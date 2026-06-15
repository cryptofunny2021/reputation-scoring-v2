# v2.0
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class ReputationScoring(gl.Contract):
    scores: TreeMap[Address, u256]
    # token_address: Address   # فعلاً کامنت شد تا Deploy راحت بشه

    def __init__(self):
        pass

    @gl.public.write
    def record_action(self, value: u256) -> None:
        user = gl.message.sender_address
        current = self.scores.get(user, u256(0))
        self.scores[user] = current + value

    @gl.public.view
    def my_score(self) -> u256:
        user = gl.message.sender_address
        return self.scores.get(user, u256(0))
