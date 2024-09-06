def triples_sum_to_zero(lst):
    # Using recursion to fix two elements and check the third one
    return any(lambda x, y, z: x + y + z == 0 for x in lst for y in lst if x != y for z in lst if x != z and y != z)