
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Create a queue to hold the remaining numbers
    queue = []

    # Find the largest number that is less than the larger of a and b
    largest_number = max(a, b)

    # Sort the remaining numbers in ascending order
    sorted_numbers = sorted(range(a, largest_number + 1))

    # Pop the even digits from the sorted numbers
    for i in range(len(sorted_numbers) // 2):
        queue.append(sorted_numbers[i])

    # Pop the even digits from the remaining numbers
    for i in range(len(queue) // 2):
        queue.append(queue.pop())

    # Return the remaining numbers in the queue
    return queue
