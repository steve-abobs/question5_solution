def min_path_with_trace(triangle):
    n = len(triangle)
    dp = [row[:] for row in triangle]
    path = [[[] for _ in row] for row in triangle]

    for j in range(len(dp[-1])):
        path[-1][j] = [dp[-1][j]]

    for i in range(n - 2, -1, -1):
        for j in range(len(dp[i])):
            if dp[i + 1][j] < dp[i + 1][j + 1]:
                dp[i][j] += dp[i + 1][j]
                path[i][j] = [triangle[i][j]] + path[i + 1][j]
            else:
                dp[i][j] += dp[i + 1][j + 1]
                path[i][j] = [triangle[i][j]] + path[i + 1][j + 1]

    return dp[0][0], path[0][0]
