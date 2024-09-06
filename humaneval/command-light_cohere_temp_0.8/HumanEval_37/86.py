```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    Return:
    list(l)
    l = l.sort_even()
   
    odd = [i for i in range(len(l)) if l[i] % 2 == 1]
    l = [l[i] for i in odd] + [l[i] for i in range(len(l)) if l[i] % 2 == 0]
    return l

# Test suite
test_suite = []
test_suite.add_case = [
    [1, 2, 3],
    [5, 6, 3, 4]]
test_suite.add_case = [
    [1, 3, 2],
    [4, 5, 6]]
test_suite.add_case = [
    [1, 2, 3, 4, 5, 6],
    [2, 6, 5, 4, 3, 1]]
test_suite.add_case = [
    [1, 2, 3, 4, 5, 6],
    [1, 4, 3, 5, 2, 6]]

def test_sort_even():
    test_suite.add_case(test_case)
    test_suite.add_case(test_case)
    test_suite.add_case(test_case)
    test_suite.add_case(test_case)
    test_suite.add_case(test_case)
    test_suite.add_case(test_case)
    test_suite.sort_even()
   
```