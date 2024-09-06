from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_list = a.split()
    b_list = b.split()

    result = ''
    for i in range(len(a_list)):
        xor_result = 0
        for j in range(len(b_list)):
            if a_list[i] == b_list[j]:
                xor_result |= 1 << (len(a_list) - i - 1)
            else:
                xor_result |= 1 << (len(a_list) - i - 1)
        result += str(xor_result)

    return result


def main():
    print('Hello, World!')


if __name__ == '__main__':
    main()