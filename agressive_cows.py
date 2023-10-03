def can_place_cows(stalls, cows, min_distance):
    placed_cows = 1
    prev_position = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - prev_position >= min_distance:
            placed_cows += 1
            prev_position = stalls[i]

            if placed_cows == cows:
                return True

    return False

def aggressive_cows(stalls, cows):
    stalls.sort()

    # Define the search range
    low = 1
    high = stalls[-1] - stalls[0]

    max_min_distance = 0

    while low <= high:
        mid = (low + high) // 2

        if can_place_cows(stalls, cows, mid):
            max_min_distance = mid
            low = mid + 1
        else:
            high = mid - 1

    return max_min_distance

# Example usage
stalls = [1, 2, 4, 8, 9]
cows = 3

result = aggressive_cows(stalls, cows)
print("The maximum minimum distance between cows is:", result)
