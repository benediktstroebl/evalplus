
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # Set the left pointer to 0 and the right pointer to the last element
    # in the array.
    left_ptr = 0
    right_ptr = len(arr) - 1

    # Our goal is to find the largest index of an element which is not
    # greater than or equal to the element immediately preceding it.
    # If no such element exists, return -1.
    # If one such element exists, return the index of that element.
    #
    # So, we know that the element at index 0 is the only element in
    # the array which is not greater than or equal to the element
    # immediately preceding it. Since it is the only element,
    # we can return 0 and be done with it.
    #
    # If the element at index 0 is not the largest element in the array,
    # we will need to find the largest element.
    #
    # How do we do that?
    # We keep track of the largest element as we traverse through the array.
    # If we find an element which is greater than or equal to the largest
    # element, we update the largest element.
    #
    # The largest element is initially set to the first element in the array.
    #
    # The moment we find an element which is greater than or equal to the
    # largest element, we know that this is the largest element.
    # So, we can return the index of the largest element.

    # Is arr[0] the largest element in the array?
    if arr[0] >= arr[left_ptr + 1]:
        return 0

    # Set largest element to arr[0]
    largest_element = arr[0]

    # Now, we need to traverse through the array and find the largest
    # element.
    while left_ptr < right_ptr:
        # If arr[left_ptr] >= arr[left_ptr + 1]
        if arr[left_ptr] >= arr[left_ptr + 1]:
            # If arr[left_ptr] is the largest element in the array,
            # return its index.
            if arr[left_ptr] == largest_element:
                return left_ptr
           
