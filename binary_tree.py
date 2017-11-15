#!/usr/bin/env python3

class BinaryTree(object):
    '''Makes a binary tree object'''

    def __init__(self):
        '''Constructor'''
        self.root = None


    def set(self, key, value):
        node = Node(key, value)

        if self.root is None:
            self.root = node

        else:
            self._add_node(self.root, node)


    def _add_node(self, oldnode, newnode):
        if newnode.key >= oldnode.key:
            if oldnode.right is not None:
                self._add_node(oldnode.right, newnode)
            else:
                oldnode.right = newnode
                newnode.parent = oldnode
        else:
            if oldnode.left is not None:
                self._add_node(oldnode.left, newnode)
            else:
                oldnode.left = newnode
                newnode.parent = oldnode


    def get(self, key):
        pass


    def remove(self, key):
        pass


    def walk_dfs_inorder(self, node):
        if(node != None):
            self.walk_dfs_inorder(node.left)
            print('{}'.format(node.value))
            self.walk_dfs_inorder(node.right)


    def walk_dfs_preorder(self, node):
        if(node != None):
            print('{}'.format(node.value))
            self.walk_dfs_preorder(node.left)
            self.walk_dfs_preorder(node.right)


    def walk_dfs_postorder(self, node):
        if(node != None):
            self.walk_dfs_postorder(node.left)
            self.walk_dfs_postorder(node.right)
            print('{}'.format(node.value))


    def walk_bfs(self):
        pass


    def debug_print(self):
        if(self.root != None):
            self.walk_dfs_inorder(self.root)


    def _replace_node(self, oldnode, newnode):
        pass


    def _find(self, key):
        pass


class Node(object):
    '''Creates a node on the binary tree'''

    def __init__(self, key, value, parent=None, left=None, right=None):
        '''Constructor'''
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
