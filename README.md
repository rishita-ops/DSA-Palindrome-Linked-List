# DSA — Palindrome Linked List

A Python implementation that determines whether a singly linked list is a **palindrome** — reading the same forwards and backwards — using a **value-extraction and slice-comparison** approach. This is the second Python program in this series and a natural companion to both the string palindrome checker and the linked list reversal program. It demonstrates how Python's list slicing enables a clean, readable solution that trades space for code simplicity, and sets up the contrast with the optimal O(1)-space slow/fast pointer approach.

---

## Problem Statement

Given a singly linked list, determine whether its values form a palindrome — the same sequence read from head to tail as from tail to head.

**The hardcoded test list:**
```
1 → 2 → 2 → 1 → None
```

**Output:**
```
The linked list IS a palindrome ✅
```

---

## The Code

```python
# Define class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create linked list
ele1 = Node(1)
ele2 = Node(2)
ele3 = Node(2)
ele4 = Node(1)

# Connect nodes
ele1.next = ele2
ele2.next = ele3
ele3.next = ele4

# Palindrome Check Function
def is_palindrome(head):
    values = []
    current = head
    # Collect all values into a list
    while current:
        values.append(current.value)
        current = current.next
    # Compare list with its reverse
    return values == values[::-1]

# Test
if is_palindrome(ele1):
    print("The linked list IS a palindrome ✅")
else:
    print("The linked list is NOT a palindrome ❌")
```

---

## Structural Improvements Over the Previous Linked List Program

This is the second linked list program in this series. Compared to the Reverse Linked List program, this one introduces two meaningful structural improvements:

| Aspect | Reverse Linked List (prev) | **This Program** |
|--------|--------------------------|-----------------|
| Core logic location | Inline in `main` body | Encapsulated in `is_palindrome()` function |
| Print method | Hardcoded chained `.next` | Traversal loop inside function |
| Traversal | Manual 4-line chain | `while current:` loop — scales to any size |
| Return value | None (side-effect only) | `bool` — clean, testable |
| Reusability | Single-use script | `is_palindrome()` callable on any head node |

The function-based approach is the correct way to structure linked list operations — each operation becomes an independently callable, testable unit.

---

## The Test List — Hardcoded Palindrome

The list `1 → 2 → 2 → 1` is deliberately chosen to be a palindrome:

```python
ele1 = Node(1)
ele2 = Node(2)
ele3 = Node(2)   # ← same value as ele2
ele4 = Node(1)   # ← same value as ele1
```

This tests the **even-length palindrome** case — no middle element, two symmetric halves. Testing with a non-palindrome (e.g., `1 → 2 → 3 → 1`) requires only changing `ele3`'s value.

Common palindrome test cases:

| List | Length | Type | Palindrome? |
|------|--------|------|-------------|
| `1 → 2 → 2 → 1` *(this code)* | 4 | Even | ✅ |
| `1 → 2 → 1` | 3 | Odd | ✅ |
| `1 → 2 → 3 → 2 → 1` | 5 | Odd | ✅ |
| `1 → 2 → 3 → 1` | 4 | Even | ❌ |
| `1` | 1 | Single | ✅ |

---

## How `is_palindrome()` Works

```python
def is_palindrome(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values == values[::-1]
```

**Three steps:**

1. **Extract** — traverse the linked list from head to tail, appending each node's value to `values`. After traversal: `values = [1, 2, 2, 1]`.
2. **Reverse** — `values[::-1]` creates a new reversed copy of the list: `[1, 2, 2, 1]`.
3. **Compare** — `values == values[::-1]` checks element-by-element equality. Returns `True` if they match, `False` otherwise.

The palindrome check is reduced to a **Python list equality comparison** — leveraging built-in `==` which compares lists element-wise in O(n).

---

## The `values[::-1]` Slice — Python's Idiomatic Reverse

```python
values[::-1]
```

This is Python's **extended slice syntax**: `[start:stop:step]`. With `step = -1` and both `start` and `stop` omitted, it returns a **new list** containing all elements in reverse order.

```python
values = [1, 2, 2, 1]
values[::-1]     # → [1, 2, 2, 1]  (new list, original unchanged)
```

It is equivalent to — but cleaner than — any of these alternatives:

```python
list(reversed(values))          # using built-in reversed()
values.copy()[::-1]             # explicit copy then slice
[values[i] for i in range(len(values)-1, -1, -1)]   # list comprehension
```

`values[::-1]` is the idiomatic Python choice — concise, readable, and well-known to any Python developer.

**Important:** `[::-1]` creates a **copy** — it does not modify `values` in place. The original list is preserved, which is why the comparison `values == values[::-1]` is valid and correct.

---

## Algorithm (Pseudocode)

```
function is_palindrome(head):
    values ← []
    current ← head

    while current is not None:
        append current.value to values
        current ← current.next

    return values == reverse(values)
```

---

## Dry Run

**List:** `1 → 2 → 2 → 1 → None`

**Traversal loop:**

| Step | `current.value` | `values` after append |
|------|-----------------|-----------------------|
| 1    | 1               | `[1]` |
| 2    | 2               | `[1, 2]` |
| 3    | 2               | `[1, 2, 2]` |
| 4    | 1               | `[1, 2, 2, 1]` |
| 5    | `None` → exit   | `[1, 2, 2, 1]` |

**Comparison:**
```
values         = [1, 2, 2, 1]
values[::-1]   = [1, 2, 2, 1]
[1,2,2,1] == [1,2,2,1]  →  True
```

**Output:** `The linked list IS a palindrome ✅`

---

**Non-palindrome test — `1 → 2 → 3 → 1`:**

```
values         = [1, 2, 3, 1]
values[::-1]   = [1, 3, 2, 1]
[1,2,3,1] == [1,3,2,1]  →  False
```

**Output:** `The linked list is NOT a palindrome ❌`

---

## Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time   | **O(n)** — one full traversal to extract values; O(n) for slice copy; O(n) for comparison — total O(n) |
| Space  | **O(n)** — `values` list stores all `n` node values; `values[::-1]` creates a second O(n) copy |

> The space cost is the key limitation of this approach. A linked list with 10 million nodes would require storing 10 million values twice simultaneously. The O(1)-space approach described below addresses this.

---

## The O(1)-Space Approach — Slow/Fast Pointer

The standard optimal solution uses **Floyd's slow/fast pointer technique** to find the midpoint, reverses the second half in place, then compares both halves — all without a value array:

```python
def is_palindrome_optimal(head):
    # Step 1: Find the middle using slow/fast pointers
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    prev, current = None, slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Step 3: Compare first half and reversed second half
    left, right = head, prev
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True
```

| Approach | Time | Space | Modifies list? |
|----------|------|-------|---------------|
| Value extraction (this repo) | O(n) | O(n) | ❌ No |
| Slow/fast pointer (optimal) | O(n) | O(1) | ✅ Yes — second half reversed |

The value-extraction approach is simpler, more readable, and preserves the original list. The slow/fast approach is optimal for memory-constrained environments and is the expected answer in most interview settings.

---

## Relationship to Other Programs in This Series

This program sits at the intersection of three earlier programs:

| Earlier Program | Connection |
|-----------------|------------|
| **Palindrome String Checker** | Same concept — comparing a sequence to its reverse — applied to a different data structure |
| **Reverse Linked List** | The optimal O(1) solution uses the reversal algorithm from that program as Step 2 |
| **Reverse Array (print-reverse)** | `values[::-1]` is the Python equivalent of the backward traversal print — same idea, different form |

---

## Edge Cases

| Scenario | `values` after traversal | Result |
|----------|--------------------------|--------|
| Empty list (`head = None`) | `[]` | `[] == []` → `True` — empty list is a palindrome by convention ✅ |
| Single node `[5]` | `[5]` | `[5] == [5]` → `True` ✅ |
| Two equal nodes `[3, 3]` | `[3, 3]` | `True` ✅ |
| Two unequal nodes `[3, 4]` | `[3, 4]` | `[3,4] == [4,3]` → `False` ✅ |
| Odd-length palindrome `[1,2,1]` | `[1,2,1]` | `True` ✅ |
| All identical values `[5,5,5,5]` | `[5,5,5,5]` | `True` ✅ |

---

## Repository Structure

```
DSA-Palindrome-Linked-List/
│
├── palindrome_linked_list.py     # Main Python implementation
└── README.md                     # Project documentation
```

---

## How to Run

**Prerequisites:** Python 3.x

```bash
# Clone the repository
git clone https://github.com/rishita-ops/DSA-Palindrome-Linked-List.git
cd DSA-Palindrome-Linked-List

# Run
python palindrome_linked_list.py
```

**Expected Output:**
```
The linked list IS a palindrome ✅
```

---

## Key Concepts Covered

- **Value extraction traversal** — collecting linked list values into a Python list using `while current:`
- **`values[::-1]` extended slice** — Python's idiomatic O(n) list reversal; creates a new copy
- **List equality comparison** — Python's `==` on lists compares element-wise in O(n)
- **Function encapsulation** — `is_palindrome()` as a reusable, testable unit returning `bool`
- **Even-length palindrome** — `1→2→2→1` as the test case; no middle element
- **O(n) space trade-off** — readable solution at the cost of storing all values twice
- **Slow/fast pointer** — the O(1)-space optimal alternative that reverses the second half in place
- **`while current:` traversal** — Pythonic loop equivalent to `while current is not None:`

---

## Why This Problem Matters in DSA

| Problem / Concept | Connection |
|-------------------|------------|
| **LeetCode #234** (Palindrome Linked List) | This exact problem — both approaches are standard solutions |
| **LeetCode #206** (Reverse Linked List) | Used as a subroutine in the O(1)-space solution |
| **LeetCode #876** (Middle of the Linked List) | Slow/fast pointer to find midpoint — Step 1 of the optimal approach |
| **LeetCode #125** (Valid Palindrome) | Same palindrome logic applied to a string with character filtering |
| **Floyd's Cycle Detection** | The slow/fast pointer pattern — also used to detect cycles in linked lists (LeetCode #141) |
| **Stack-based palindrome check** | Push first half onto stack, compare with second half — O(n) space alternative |
| **Deque-based palindrome check** | Append to both ends, pop and compare — same idea in a different structure |

The palindrome linked list problem sits at the crossroads of three fundamental skills — linked list traversal, reversal, and the palindrome check — making it one of the highest-value problems for consolidating multiple DSA concepts simultaneously.

---

## Contributing

Contributions are welcome. Consider adding:
- An **O(1)-space slow/fast pointer version** for comparison
- A **recursive palindrome checker** using the call stack implicitly
- A version that **restores the original list** after the O(1) check
- A general `LinkedList` class with `append` and `is_palindrome` methods
- Implementations in C++, Java, or JavaScript

```bash
git checkout -b feature/your-feature
git commit -m "Add: your feature description"
git push origin feature/your-feature
# Then open a Pull Request
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

*Part of a structured DSA practice series — fundamentals, done right.*
