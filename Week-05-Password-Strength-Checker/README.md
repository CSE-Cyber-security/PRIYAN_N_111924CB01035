# Week 5 – Password Strength Checker

A Python program that checks a password against basic strength rules and classifies it as Weak, Medium, or Strong.

## Rules Checked

1. At least 8 characters
2. Contains an uppercase letter
3. Contains a lowercase letter
4. Contains a number
5. Contains a special character

## Strength Classification

- 0–2 rules passed: Weak
- 3–4 rules passed: Medium
- 5 rules passed: Strong

## Features

- Shows which password requirements are satisfied.
- Hides password input while typing using Python's `getpass` module.
- Does not save or send the password anywhere.
- Uses only Python built-in modules.

## Folder Structure

```text
Week-05-Password-Strength-Checker/
├── password_strength_checker.py
├── README.md
└── screenshots/
    └── 01-password-strength-checker.png
```

## How to Run

```bash
python password_strength_checker.py
```

Use `python3` instead of `python` on systems where needed.

## Example Output

```text
PASSWORD STRENGTH CHECKER

Enter a password: ************

Password Strength: Strong

Password Requirements:
PASS - At least 8 characters
PASS - Contains an uppercase letter
PASS - Contains a lowercase letter
PASS - Contains a number
PASS - Contains a special character
```

The example is illustrative. The actual password is hidden while typing.

## Concepts Used

- Python functions
- Conditional statements
- String methods
- Loops
- `getpass` module
