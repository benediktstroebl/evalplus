
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''

    # first time to learn this kind of coding
    # it could be an interesting topic to write a book for
    # I need to write some test cases for this
    # and I will do that

    import unittest

    class TestStrangeSortList(unittest.TestCase):
        def test_1(self):
            self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

        def test_2(self):
            self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

        def test_3(self):
            self.assertEqual(strange_sort_list([]), [])

    if __name__ == '__main__':
        unittest.main()

    return lst
