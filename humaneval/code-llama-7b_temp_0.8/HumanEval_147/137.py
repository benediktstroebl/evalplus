
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    def get_cubes(n):
        """
        Compute the cubes of the numbers between 1 and n
        """
        return [i * i * i for i in range(1, n+1)]

    def get_sliced_cubes(cubes, n):
        """
        Compute the number of sliced cubes (i, j, k) with k < n
        """
        #TODO: write docstring
        count = 0
        for i in range(len(cubes)):
            for j in range(i+1, len(cubes)):
                if cubes[j] - cubes[i] < n:
                    count += 1
        return count

    def get_triples(cubes, n):
        """
        Compute the number of triples (a[i], a[j], a[k]) with i < j < k, 
        where i, j, k are indices in the cubes list
        """
        #TODO: write docstring
        count = 0
        for i in range(len(cubes)-2):
            for j in range(i+1, len(cubes)-1):
                for k in range(j+1, len(cubes)):
                    if (cubes[j] - cubes[i] == cubes[k] - cubes[j]):
                        count += 1
        return count

    cubes = get_cubes(n)
    sliced_cubes = get_sliced_cubes(cubes, n)
    return sliced_cubes * 3 // 2

