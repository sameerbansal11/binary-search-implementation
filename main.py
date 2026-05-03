#!/usr/bin/env python3
"""
binary-search-implementation
Binary Search Algorithm with step-by-step explanation output.

Author: Sameer Bansal
Reg No: RA2311032010061
College: SRM Institute of Science and Technology
Branch: B.Tech CSE (IoT) | Batch: 2023-2027
"""


def binary_search(arr, target):
    """
    Iterative Binary Search
    Returns: (index, steps) or (-1, steps) if not found
    """
    left, right = 0, len(arr) - 1
    steps = 0

    print(f"\n🔍 Searching for: {target}")
    print(f"📋 Array: {arr}")
    print("-" * 50)

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        print(
            f"Step {steps}: left={left}, right={right}, mid={mid} → arr[mid]={arr[mid]}"
        )

        if arr[mid] == target:
            print(f"\n✅ Found {target} at index {mid} in {steps} step(s)!")
            return mid, steps
        elif arr[mid] < target:
            print(f"   ➡️  {arr[mid]} < {target}, search RIGHT half")
            left = mid + 1
        else:
            print(f"   ⬅️  {arr[mid]} > {target}, search LEFT half")
            right = mid - 1

    print(f"\n❌ {target} not found in array after {steps} step(s).")
    return -1, steps


def binary_search_recursive(arr, target, left, right, steps=0):
    """
    Recursive Binary Search
    Returns: (index, steps) or (-1, steps) if not found
    """
    if left > right:
        return -1, steps

    steps += 1
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid, steps
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, steps)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, steps)


def linear_search(arr, target):
    """Linear Search for comparison"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def compare_performance():
    """Compare Binary Search vs Linear Search"""
    import random
    import time

    arr = sorted(random.randint(1, 10000) for _ in range(1000))
    target = random.choice(arr)

    print("\n" + "=" * 50)
    print("⚡ PERFORMANCE COMPARISON (1000 elements)")
    print("=" * 50)

    # Binary Search timing
    start = time.perf_counter()
    for _ in range(10000):
        binary_search_recursive(arr, target, 0, len(arr) - 1)
    binary_time = time.perf_counter() - start

    # Linear Search timing
    start = time.perf_counter()
    for _ in range(10000):
        linear_search(arr, target)
    linear_time = time.perf_counter() - start

    print(f"🔵 Binary Search : {binary_time:.4f}s (10,000 runs)")
    print(f"🔴 Linear Search : {linear_time:.4f}s (10,000 runs)")
    print(f"🚀 Binary is {linear_time / binary_time:.1f}x faster!")


def run_tests():
    """Run test cases"""
    print("\n" + "=" * 50)
    print("🧪 RUNNING TEST CASES")
    print("=" * 50)

    tests = [
        ([1, 3, 5, 7, 9, 11, 13, 15], 7, 3),
        ([1, 3, 5, 7, 9, 11, 13, 15], 1, 0),
        ([1, 3, 5, 7, 9, 11, 13, 15], 15, 7),
        ([1, 3, 5, 7, 9, 11, 13, 15], 6, -1),
        ([42], 42, 0),
        ([], 5, -1),
    ]

    passed = 0
    for arr, target, expected in tests:
        if not arr:
            result = -1
        else:
            result, _ = binary_search_recursive(arr, target, 0, len(arr) - 1)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result == expected:
            passed += 1
        print(
            f"{status} | Array size: {len(arr):3} | Target: {target:3} | Expected: {expected:2} | Got: {result:2}"
        )

    print(f"\n📊 Results: {passed}/{len(tests)} tests passed")


def main():
    print("=" * 50)
    print("  BINARY SEARCH IMPLEMENTATION")
    print("  Author : Sameer Bansal | RA2311032010061")
    print("  College: SRMIST Kattankulathur")
    print("=" * 50)

    # Demo 1 — Iterative with step-by-step output
    arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    binary_search(arr, 23)
    binary_search(arr, 100)

    # Demo 2 — Recursive
    print("\n" + "=" * 50)
    print("🔄 RECURSIVE BINARY SEARCH")
    print("=" * 50)
    index, steps = binary_search_recursive(arr, 56, 0, len(arr) - 1)
    print(f"Target 56 → Index: {index} | Steps taken: {steps}")

    # Demo 3 — Test cases
    run_tests()

    # Demo 4 — Performance comparison
    compare_performance()

    # Interactive mode
    print("\n" + "=" * 50)
    print("🎮 INTERACTIVE MODE")
    print("=" * 50)
    print(f"Array: {arr}")
    while True:
        try:
            user_input = input("\nEnter number to search (or 'q' to quit): ").strip()
            if user_input.lower() == "q":
                print("👋 Goodbye!")
                break
            target = int(user_input)
            binary_search(arr, target)
        except ValueError:
            print("⚠️  Please enter a valid number.")


if __name__ == "__main__":
    main()
