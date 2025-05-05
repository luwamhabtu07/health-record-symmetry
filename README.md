# Health Record Symmetry Checker

## Problem
Determine if a patient's health metrics (as a singly linked list) form a symmetric pattern.

## Approach
- Find middle of linked list
- Reverse second half
- Compare both halves
- Restore list (optional)

## Time & Space Complexity
- Time: O(n)
- Space: O(1)

## Files
- `main.py`: implementation
- `test_health_record.py`: unit tests
- `flowchart.png`: process diagram
- `clarifying_questions.md`: questions asked

## Run Tests
```bash
python3 test_health_record.py
