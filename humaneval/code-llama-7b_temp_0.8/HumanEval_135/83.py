
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Boundary conditions
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] == 1 else -1

    # Hypothesis
    # arr[i] >= arr[i - 1]
    # arr[i] < arr[i + 1]

    # Induction
    # arr[i] >= arr[i - 1]
    # arr[i] < arr[i + 1]
    # i <= len(arr) - 2

    # Base case: arr[len(arr) - 1] < arr[len(arr) - 2]
    if arr[len(arr) - 1] >= arr[len(arr) - 2]:
        return len(arr) - 1

    # Induction
    # 1. arr[i] >= arr[i - 1]
    # 2. arr[i] < arr[i + 1]
    # 3. arr[i] < arr[i + 2]
    # i <= len(arr) - 3

    # Recursive cases
    if arr[len(arr) - 2] >= arr[len(arr) - 3]:
        return len(arr) - 1

    if arr[len(arr) - 1] < arr[len(arr) - 2]:
        return can_arrange(arr[:len(arr) - 1])

    if arr[len(arr) - 1] < arr[len(arr) - 2]:
        return can_arrange(arr[:len(arr) - 1])

    return -1
