# test_dummy.py

from scheduler.core.abstract_node import AbstractNode
from scheduler.core.abstract_network import AbstractNetwork
from scheduler.core.observer import Observer

class DummyNode(AbstractNode):
    def __init__(self, name):
        super().__init__(name)
        self.mailbox = []

    def process_action(self):
        return None

class DummyNetwork(AbstractNetwork):
    def __init__(self):
        super().__init__()
        self.nodes = [DummyNode("Node1"), DummyNode("Node2")]

if __name__ == "__main__":
    network = DummyNetwork()
    observer = Observer(network)
    observer.run()
    print("Тестова симуляція завершена")