import unittest
from main import Node, isHealthRecordSymmetric

class TestHealthRecordSymmetry(unittest.TestCase):
    def build_linked_list(self, values):
        if not values:
            return None
        head = Node(values[0])
        curr = head
        for val in values[1:]:
            curr.next = Node(val)
            curr = curr.next
        return head

    # Normal test cases
    def test_symmetric_even(self):
        head = self.build_linked_list([80, 90, 90, 80])
        self.assertTrue(isHealthRecordSymmetric(head))

    def test_symmetric_odd(self):
        head = self.build_linked_list([70, 80, 70])
        self.assertTrue(isHealthRecordSymmetric(head))

    def test_not_symmetric(self):
        head = self.build_linked_list([100, 110, 120])
        self.assertFalse(isHealthRecordSymmetric(head))

    # Edge test cases
    def test_empty_list(self):
        head = self.build_linked_list([])
        self.assertTrue(isHealthRecordSymmetric(head))

    def test_single_node(self):
        head = self.build_linked_list([90])
        self.assertTrue(isHealthRecordSymmetric(head))

    def test_two_different_nodes(self):
        head = self.build_linked_list([90, 100])
        self.assertFalse(isHealthRecordSymmetric(head))

if __name__ == "__main__":
    unittest.main()
