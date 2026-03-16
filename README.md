<div align="center">

```
╔══════════════════════════════════════════════════╗
║                                                  ║
║   1 → 2 → 2 → 1   PALINDROME LINKED LIST        ║
║   ↑               CHECK  in Python              ║
║   └───────────────────────────────┘              ║
╚══════════════════════════════════════════════════╝
```

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)
![DSA](https://img.shields.io/badge/Topic-Linked%20Lists-f59e0b?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-22c55e?style=flat-square)

*A lightweight Python implementation to detect whether a singly linked list reads the same forwards and backwards.*

</div>

---

## 🪞 What is this?

This project builds a **singly linked list** and checks if it forms a **palindrome** — a sequence that is identical whether read left-to-right or right-to-left.

```
1 → 2 → 2 → 1   ✅  Palindrome
1 → 2 → 3 → 4   ❌  Not a palindrome
```

A deceptively simple problem with elegant solutions — and a staple of technical interviews worldwide.

---

## 🧠 How it Works

### Step 1 — Collect

Traverse the linked list and dump every node value into a Python list:

```
Node traversal:   [ 1 ] → [ 2 ] → [ 2 ] → [ 1 ]
Collected list:   [1, 2, 2, 1]
```

### Step 2 — Compare

Check whether the collected list equals its own reverse:

```
Original:   [1, 2, 2, 1]
Reversed:   [1, 2, 2, 1]
              ✓  ✓  ✓  ✓  →  Palindrome ✅
```

A non-palindrome would fail at the first mismatch:

```
Original:   [1, 2, 3, 4]
Reversed:   [4, 3, 2, 1]
              ✗           →  Not a palindrome ❌
```

---

## 📁 File Structure

```
📦 palindrome-linked-list/
 ┗ 📄 palindrome_check.py    ← Full implementation
```

---

## 🚀 Getting Started

No dependencies. Just Python.

```bash
# Clone the repo
git clone https://github.com/your-username/palindrome-linked-list.git

# Navigate into it
cd palindrome-linked-list

# Run it
python palindrome_check.py
```

### Output

```
The linked list IS a palindrome ✅
```

---

## 🔍 Code Walkthrough

```python
# 1. The Node class — each node holds a value and points to the next
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 2. Build the list: 1 → 2 → 2 → 1 (a classic palindrome)
ele1 = Node(1)
ele2 = Node(2)
ele3 = Node(2)
ele4 = Node(1)

ele1.next = ele2
ele2.next = ele3
ele3.next = ele4

# 3. The palindrome check
def is_palindrome(head):
    values = []
    current = head

    while current:
        values.append(current.value)   # Collect values
        current = current.next

    return values == values[::-1]      # Compare with reverse

# 4. Test it
if is_palindrome(ele1):
    print("The linked list IS a palindrome ✅")
else:
    print("The linked list is NOT a palindrome ❌")
```

---

## ⏱ Complexity

| | Complexity | Notes |
|---|---|---|
| **Time** | `O(n)` | Single traversal to collect values |
| **Space** | `O(n)` | Extra list stores all node values |

> 💬 **Want `O(1)` space?** It's possible — reverse only the second half of the list in-place, compare, then restore. See [Extensions](#-possible-extensions) below.

---

## 💡 Key Concepts

- **Singly Linked List** — nodes linked in one direction only
- **Palindrome Property** — a sequence identical to its own reverse
- **List slicing** — Python's `[::-1]` creates a reversed copy in one line
- **Two-pass approach** — collect first, compare second

---

## 🧪 Test Cases

| Linked List | Expected Output |
|---|---|
| `1 → 2 → 2 → 1` | ✅ Palindrome |
| `1 → 2 → 1` | ✅ Palindrome |
| `7 → 7` | ✅ Palindrome |
| `5` | ✅ Palindrome (single node) |
| `1 → 2 → 3 → 4` | ❌ Not a palindrome |
| `1 → 2 → 3 → 2` | ❌ Not a palindrome |

---

## 🎯 Why This Problem Matters

Palindrome detection on a linked list is harder than it looks — you can't index into it like an array. This problem tests:

- Linked list traversal
- Understanding of Python slicing
- Awareness of time vs. space trade-offs
- Ability to reason about symmetry in data structures

It appears regularly in interviews at **Google**, **Amazon**, **Microsoft**, and is a staple on **LeetCode (#234)**.

---

## 🌱 Possible Extensions

- [ ] Wrap logic into a `LinkedList` class with an `.is_palindrome()` method
- [ ] Implement the `O(1)` space solution using slow/fast pointers + in-place reversal
- [ ] Support palindrome detection for string-valued nodes (e.g. `"racecar"`)
- [ ] Add full test suite with `pytest`
- [ ] Visualize the comparison step-by-step in the terminal

---

## 📜 License

MIT — free to use, learn from, and build upon.

---

<div align="center">

*Symmetry is beautiful. So is clean code.*

</div>
