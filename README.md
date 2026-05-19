# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
This game challenges user to guess a number based on the difficulty level that the user picked, for each difficulty level the number range and allowed attempts are different. Once the user selects difficulty level, they can enter their guess based on the given range, if they guess it correctly, the success message is displayed and the total score is displayed, to restart the game, user has to click on restart to continue playing. if they guess it incorrectly within the attempts, the failure message is displayed and total score is also displayed, to restart the game, user needs to clicks on start new game.
- [X] Detail which bugs you found.
I identified four bugs: 
1. The hint displayed was in backwards order.
2. The range for each difficulty level and attempts allowed were not correctly reflected on main page and sidebar.
3. The start new game button did not start a new game.
4. The hint checkbox state was not preserved across page reruns, causing hints to flicker and disappear.
- [X] Explain what fixes you applied.
1. For the first one I changed the logic to show correct message: if the guess is greater than secret, display "Too high" (📉 Go LOWER!), if the guess is lower than secret, display "Too low" (📈 Go HIGHER!).
2. I changed the range from the original hardcoded 1 to 100 static message to dynamic {low} to {high} based on difficulty level.
3. I added a session status "playing" that resets when the user clicks on "New Game", allowing them to start a new game after winning or losing.
4. I added `key="show_hint"` to the checkbox widget to ensure Streamlit preserves its state across reruns, preventing hints from flickering. 
## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
