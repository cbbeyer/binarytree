import unittest
from binary_tree import BinaryTree

# python3 -m unittest tests.py
class BinaryTreeTesting(unittest.TestCase):
    def test_create_binary_tree(self):
        binary_tree = BinaryTree()
        return binary_tree
        print('here')

    def test_add_node_to_tree(self):
        binary_tree = self.test_create_binary_tree()

        binary_tree.set('a', 'A')
        binary_tree.set('b', 'B')
        binary_tree.set('c', 'C')

        self.assertEqual(binary_tree.root.value, 'A')

    def test_add_node_check_val(self):
        binary_tree = self.test_create_binary_tree()

        binary_tree.set('a', 'A')
        binary_tree.set('b', 'B')
        binary_tree.set('c', 'C')

        self.assertEqual(binary_tree.root.right.value, 'B')

    def test_check_val_failure(self):
        binary_tree = self.test_create_binary_tree()

        binary_tree.set('a', 'A')
        binary_tree.set('b', 'B')
        binary_tree.set('c', 'C')

        self.assertEqual(binary_tree.root.right.value, 'C')

    def test_remove_node(self):
        binary_tree = self.test_create_binary_tree()

        binary_tree.set('a', 'A')
        binary_tree.set('b', 'B')
        binary_tree.set('c', 'C')

        binary_tree.remove('b')

        self.assertNotEqual(binary_tree.root.right.value, 'B')

    def test_remove_node_failure(self):
        binary_tree = self.test_create_binary_tree()

        binary_tree.set('a', 'A')
        binary_tree.set('b', 'B')
        binary_tree.set('c', 'C')

        binary_tree.remove('b')

        self.assertEqual(binary_tree.root.right.value, 'B')
