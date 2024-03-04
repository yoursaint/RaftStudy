from typing import Final
from pyraft import raft

EX_IP: Final[str]= 'localhost'
list_node = {1:f'{EX_IP}:5010', 2:f'{EX_IP}:5020', 3:f'{EX_IP}:5030'}

# list node의 k(1)와 v(2)를 하나씩 출력하여 RaftNode의 인자로 넘기고, filter를 활용해 출력되는 k를 제외한 dict(3)를 얕은 복사하여 인자로 넘김 / 인자 (1), (2), (3)
nodes = [raft.RaftNode(k, v, dict(filter(lambda k2 : k != k2[0], list_node.items()))) for k, v in list_node.items()]

# 각 노드 실행
for _node in nodes:
    _node.start()
    _node.join()

"""
#To-Do
Log 출력은 어떻게...?
"""