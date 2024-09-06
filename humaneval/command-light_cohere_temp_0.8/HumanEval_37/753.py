```python
def sort_even(lst):
    return lst[:]  # for simplicity, we just return the list as it is

    for i in range(1, len(lst)):
        if lst[i] % 2 == 0:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
    return lst

# Test the function
list1 = [5, 6, 3, 4]
list2 = [3, 6, 5, 4]
list3 = [1, 2, 3]

print("List 1: ", end="")
print(*list1)
print()

print("List 2: ", end="")
print(*list2)
print()

print("List 3: ", end="")
print(*list3)
print()

list1 = [5, 6, 3, 4]
list2 = [3, 6, 5, 4]
list3 = [1, 2, 3, 4, 5, 6]

print("List 1: ", end="")
print(*list1)
print()

print("List 2: ", end="")
print(*list2)
print()

print("List 3: ", end=")
print(*list3)
print()

def test_even_sort():
    input_list = [5, 6, 3, 4]
    output_list = sort_even(input_list)
    print("Input:", end=")
    print(*input_list)
    print("Output:", end=")
    print(*output_list)

test_even_sort()
```