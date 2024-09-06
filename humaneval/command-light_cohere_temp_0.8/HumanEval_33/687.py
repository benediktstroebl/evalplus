```python
def sort_third(lst):
    """This function sorts a list such that values divisible by three appear in their correct position.
    if len(lst) <= 1: return lst
    for i in range(len(lst)):
        if lst[i] % 3 == 0:
            lst[i] = lst[i] + 1
        else:
            lst[i] = lst[i] - 1
    return lst
# Example usage:
if __name__ == "__main__":
    test_lst = [5, 6, 3, 4, 8, 9, 2]
    print(sort_third(test_lst))
    ```