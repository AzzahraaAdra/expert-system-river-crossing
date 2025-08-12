# Expert System – Farmer, Wolf, Goat, and Cabbage Puzzle

This Python program solves the classic **Farmer, Wolf, Goat, and Cabbage** river crossing puzzle using the **Experta** library (an expert system framework).

---

## Puzzle Description
A farmer must transport a wolf, a goat, and a cabbage across a river.  
The boat can carry the farmer and **only one item** at a time.  

Rules:
- The wolf cannot be left alone with the goat (wolf will eat the goat).
- The goat cannot be left alone with the cabbage (goat will eat the cabbage).

The program uses a **knowledge-based inference engine** to find a valid solution while avoiding invalid states.

---

## Requirements
- **Python 3.8 or 3.9 recommended**  
  > The Experta library may not work on Python 3.10+ due to deprecated features in `collections`.  
  > If using Python 3.10 or newer, you may need to patch the Experta code or use an alternative rule engine such as CLIPS.
- [Experta](https://pypi.org/project/experta/) library

Install dependencies:
```bash
pip install experta
