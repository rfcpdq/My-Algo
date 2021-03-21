# time: O(n^2)
# Sorting the array will take O(n * logn)
# The searchPair() function will take O(n)
#   As we are calling searchPair() for every number in the input array,
#     this means that overall searchTriplets() will take O(n * logn + n^2),
#     which is asymptotically equivalent to O(n^2)
# space: O(n)

# element may be used multiple times
# same as bp01
# sorted first, 2 pointers from left and right move to middle
# !! skip same element to avoid duplicate triplets
# what if: [-1, -1, -1, 2] ? add [-1, -1, 2] at arr[0]

# [-3, -2, -1, 0, 1, 1, 2] 
# if arr[i] is -3 (x=-3)
# find y+z = 0-(-3)

def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        # skip same element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_pair(arr, -arr[i], i + 1, triplets)
    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            # avoid duplicate triplets
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
