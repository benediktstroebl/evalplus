
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Try to use a priority queue to do it in O(n log n) time
    # However, the code is quite complex, and we can achieve the same result in O(n) time
    # Using a queue is not necessary
    for i in range(len(lst)):
        if i % 2 == 1:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            # We replace the odd element with the previous element, which is now in the correct position
            # Now, the first two elements of the list are the correct even-odd pattern
            # We can check the rest of the list recursively using this pattern
    return lst[1] + solution([lst[2:],lst[1]])


def main():
    # Test the solution
    test_cases = [
        [5, 8, 7, 1],
        [3, 3, 3, 3, 3],
        [30, 13, 24, 321],
    ]
    for t in test_cases:
        print(t)
        print(solution(t))
    # test
    # test
    # test

if __name__ == '__main__':
    main()