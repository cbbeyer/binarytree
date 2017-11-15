from binary_tree import BinaryTree


def main():
    '''Main program'''
    binary_tree = BinaryTree()

    binary_tree.set('c', 'C')
    binary_tree.set('h', 'H')
    binary_tree.set('a', 'A')
    binary_tree.set('e', 'E')
    binary_tree.set('f', 'F')
    binary_tree.set('d', 'D')
    binary_tree.set('b', 'B')
    binary_tree.set('j', 'J')
    binary_tree.set('g', 'G')
    binary_tree.set('i', 'I')
    binary_tree.set('k', 'K')

    print('Initial tree:')
    # debug_print()

    print('\nLookups:')
    # get()
    # get()
    # get()

    print('\nBFS:')
    # walk_bfs()

    print('\nDFS inorder:')
    binary_tree.walk_dfs_inorder(binary_tree.root)

    print('\nDFS preorder:')
    binary_tree.walk_dfs_preorder(binary_tree.root)

    print('\nDFS postorder:')
    binary_tree.walk_dfs_postorder(binary_tree.root)

# Runner
if __name__ == '__main__':
    main()
