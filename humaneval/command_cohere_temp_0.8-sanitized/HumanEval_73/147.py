import unittest
def smallest_change(arr):
    return float('inf') if arr == [] else len(set(arr)) // 2