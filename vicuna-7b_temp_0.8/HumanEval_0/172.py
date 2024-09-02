from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for i in range(len-1):
        if abs(numbers[i]) - abs(numbers[i+1]) > threshold:
            return False
    return True


def main():
    numbers = List('float')
    threshold = float(input("Enter threshold value: "))

    for x in range(int(input("Enter length of list: "))):
        numbers.append(float(input("Enter number: ")))

    if has_close_elements(numbers, threshold):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()