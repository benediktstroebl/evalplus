def minPath(grid, k):
    n = len(grid)
    # Initialize the frontier with the first row of the grid
    frontier = [row[0] for row in grid]
    # Initialize the best path metric with the lexicographically smallest k-length sequence in the first row
    bestPathMetric = sorted(frontier)[:k]
    # Track the last row index visited for each cell in the best path
    lastVisitedRowIndices = {val: i for i, val in enumerate(bestPathMetric)} # i: row index, val: cell value
    # Sort the frontier based on the cell values
    frontier = sorted(frontier)
    # Track the number of times each cell value appears in the current frontier
    numAppearances = {val: len(list(filter(lambda x: x == val, frontier))) for val in frontier} # val: cell value
    
    # Iterate through the rows of the grid
    for i in range(1, n):
        # Filter out the already visited cells in the current row
        currentRow = [x for x in grid[i] if x not in bestPathMetric and not (i in lastVisitedRowIndices and grid[i][x] == grid[lastVisitedRowIndices[x]][x])]
        # Update the frontier with the current row filtered
        frontier = currentRow
        # Sort the frontier based on the cell values
        frontier = sorted(frontier)
        # Update the numAppearances for the current frontier
        numAppearances = {val: len(list(filter(lambda x: x == val, frontier))) for val in frontier} # val: cell value
        # Find the lexicographically smallest k-length sequence in the current frontier
        smallestKLengthSeq = sorted(frontier)[:k]
        # Update the best path metric and last row index visited for each cell in the best path
        for val in smallestKLengthSeq:
            lastVisitedRowIndices[val] = i
        bestPathMetric += smallestKLengthSeq
        # Remove duplicates and keep only the cells that have not been visited before
        bestPathMetric = list(set(bestPathMetric))
        # Reverse the best path metric to ensure the path is followed from the start cell
        bestPathMetric.reverse()
        # Return the best path metric
        return bestPathMetric