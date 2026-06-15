# Reputation Scoring v2.0
# Connected Reputation System for SocialFi

from genlayer import *

class ReputationScoring(gl.Contract):
    scores: TreeMap[Address, u256]
    token_address: Address

    def __init__(self, token_addr: Address):
        self.token_address = token_addr

    @gl.public.write
    def record_action(self, value: u256) -> None:
        """Record user action and update reputation"""
        user = gl.message.sender_address
        current = self.scores.get(user, u256(0))
        self.scores[user] = current + value

        # Auto reward tokens (if value is positive)
        if value > u256(0):
            try:
                token = gl.contract(self.token_address)
                token.mint(value // u256(2))  # 50% of reputation as tokens
            except:
                pass  # Safe call

    @gl.public.view
    def my_score(self) -> u256:
        """Get my reputation score"""
        return self.scores.get(gl.message.sender_address, u256(0))
