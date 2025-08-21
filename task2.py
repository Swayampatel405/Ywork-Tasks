def distribute_candies(priority):
    n = len(priority)
    candies = [1] * n 

    for i in range(1, n):
        if priority[i] > priority[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-2, -1, -1):
        if priority[i] > priority[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return candies, sum(candies)

priority = [1, 2, 2]
candies, total = distribute_candies(priority)
print("Candies distribution:", candies)
print("Total candies needed:", total)
