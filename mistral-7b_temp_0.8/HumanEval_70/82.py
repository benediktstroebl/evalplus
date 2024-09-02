
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
    # Write your code here.
    def swap(num1, num2, array):
        temp = array[num1]
        array[num1] = array[num2]
        array[num2] = temp

    def min_index(array):
        min_i = 0
        for i in range(1, len(array)):
            if array[i] < array[min_i]:
                min_i = i
        return min_i

    def max_index(array):
        max_i = 0
        for i in range(1, len(array)):
            if array[i] > array[max_i]:
                max_i = i
        return max_i

    max_i = max_index(lst)
    min_i = min_index(lst)
    if max_i == min_i:
        return lst
    swap(max_i, min_i, lst)
    return strange_sort_list(lst[:max_i]+lst[max_i+1:min_i]+lst[min_
