```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not"]

if __name__ == "__main__":
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print(unique(test_list))
    assert len(unique(test_list)) == len(set(test_list))
    ```
Do you want me to help you with any other code problem?