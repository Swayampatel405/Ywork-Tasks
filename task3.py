def maximalRectangle(matrix):
    
    rows, cols = len(matrix), len(matrix[0])
    height = [0] * cols
    left = [0] * cols
    right = [cols] * cols
    max_area = 0

    for r in range(rows):
        cur_left, cur_right = 0, cols

        # Update height
        for c in range(cols):
            if matrix[r][c] == "1":
                height[c] += 1
            else:
                height[c] = 0

        # Update left boundary
        for c in range(cols):
            if matrix[r][c] == "1":
                left[c] = max(left[c], cur_left)
            else:
                left[c] = 0
                cur_left = c + 1

        # Update right boundary
        for c in range(cols - 1, -1, -1):
            if matrix[r][c] == "1":
                right[c] = min(right[c], cur_right)
            else:
                right[c] = cols
                cur_right = c

        # Compute area
        for c in range(cols):
            max_area = max(max_area, (right[c] - left[c]) * height[c])

    return max_area


# Example
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

print(maximalRectangle(matrix))  # Output: 6
