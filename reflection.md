# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game is full of glitches, it allows user to go out of range and the guess hints were not accurate. 
1. the range was 1 to 100 but when I enter 111, it showed go higher.
2. when I clicked start new game after first game attempt ran out, it did not start a new game. New game started after refreshing the page and all the previous records were gone.
3. When I clicked submit Guess, sometimes it doesn't automatically submit it, after you click it the hint disappear and then it goes through. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. the range was 1 to 100 but when I enter 111, it showed go higher.
2. when I clicked start new game after first game attempt ran out, it did not start a new game. New game started after refreshing the page and all the previous records were gone.
3. The Settings sidebar has three different levels and it explains how many attempts allowed and the range, whatever is shown on the sidebar is different than than on the main page. 
4. game status is not displayed on main page
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Haiku 4.5 and Copilot CLI for agent mode
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When I used Claude Haiku 4.5, it correctly identified bugs and help me fix three bugs that I identified.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I used Copilot CLI Agent Mode it changed all my fixes from the issues that I identified. and I accepted I realize all my changes were gone and Copilot's changes were very misleading and hard to understand, after merging the code, I revert it back.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I asked Claude to help me create test cases related to that fix and all the tests passed and I also tested on the UI. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested the range on sidebar and range on main page, now it matched and also the attempt allowed also aligned.
- Did AI help you design or understand any tests? How?
Yes, I asked Claude to be specific on creating the test cases, target on the fixes that I did.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
