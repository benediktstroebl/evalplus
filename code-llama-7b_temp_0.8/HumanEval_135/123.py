
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Initialize the array
    arr.insert(0, 0)

    # Push the values in a stack
    st = []
    for i in range(len(arr)):
        st.append(arr[i])

    # Iterate through the stack and update the index
    # of the largest element that's lesser than it
    for i in range(len(arr)):
        arr[i] = st[-1]
        st.pop()
        for j in range(len(st)):
            if st[-1] < arr[i]:
                arr[i] = st[-1]
                st.pop()
            else:
                break

    print(arr)

