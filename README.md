# The Monty Hall Problem Simulation
A Python simulation to prove The Monty Hall Problem.


## Introduction
The Monty Hall Problem is a fascinating and fun brain teaser in the form a probability puzzle. The puzzle proposes the following scenario:

*Suppose you are on a game show and are presented with three closed doors. Behind one door is a million dollars. Behind the other two remaining doors are goats. You make a selection of one of these doors. After your selection, the game show host ups the ante by opening one of the doors you didn't choose, revealing a goat. He then offers you a choice; either stay with your original door, or switch to the other remaining door. What do you do?*

Now believe it or not, there is a correct answer to this. Intuitively, it would appear that there is neither a right or wrong answer, as you would think that your odds are 50/50, simply because of the fact that you either have to make a decision to stay with your door or switch. You are faced with only 2 choices, therefore you are facing 50/50 odds. How can there be a *correct* answer at all? Well it turns out there is, and the answer is to switch!


## Explanation
So why is switching the correct answer? At the end of the day, we have 2 doors to choose from. One has the money, and the other has the goat. These are 50/50 odds, surely. Well probability says otherwise!

When we started the game, we didn't have just two doors, we had three. When you make your first initial choice, the odds of you choosing the door with the money is 1 in 3 (1/3) (33.33%). That means there is a 66.66% chance that you **did not** pick the door with the money. That's a 66.66% chance that the door with the money is inside the other two doors you didn't choose. When one of those two doors are revealed to have the goat, that means the last remaining door has a 66.66% chance of having the million dollars.

Now for some of you, things may have started to click already. But for others, this may still be challenging to wrap your head around. Don't worry, I was exactly the same! So to make this even clearer to understand, we will extend our doors from a total of three, to a total of a thousand! Let's walk through this together...

You have a thousand (1000) doors, and you select just one (1) of those. What are the chances out of a thousand doors, that your selection just so happens to be the door with the million dollars? Pretty unlikely, I'm sure you would agree. A 1/1000, otherwise known as a 0.1% chance! It's not hard to understand now, that the door with the million dollars is very likely to be in the other 999 doors. A 99.9% chance to be exact! If the game show host now elimates 998 of those doors that contain the goats, leaving one remaining door, then that door is 99.9% likely to be the door with the money inside. This is a lot easier to see when you extend this game to a thousand doors. When you are dealing with just three doors, it's a little harder to imagine. But hopefully you can now see.


## Fun fact
The puzzle was introduced by **Steve Selvin** in a series of letters to The American Statistician in 1975, describing it as the "*Monty Hall problem*". The puzzle gained widespread attention when **Marilyn vos Savant**, a columnist for Parade magazine, wrote about it in 1990. Her solution, which correctly advised switching doors, sparked significant public debate and confusion.

**Quote from Wikipedia source** [https://en.wikipedia.org/wiki/Monty_Hall_problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)

*"Many readers of Savant's column refused to believe switching is beneficial and rejected her explanation. After the problem appeared in Parade, approximately 10,000 readers, including nearly 1,000 with PhDs, wrote to the magazine, most of them calling Savant wrong. Even when given explanations, simulations, and formal mathematical proofs, many people still did not accept that switching is the best strategy. Paul Erdős, one of the most prolific mathematicians in history, remained unconvinced until he was shown a computer simulation demonstrating Savant's predicted result."*

So there you have it! This problem and it's solution even had the best mathematicians in the world unconvinced that switching would give the best odds of winning. So don't feel too bad on yourself if this had you stumped. It certainly made me feel better knowing I was not the only one!


## Fun extras: Simulation
To finish off, I will leave all of you a computer simulation I wrote in Python, which visually shows you the result of either switching, or not switching. As **Savant** demonstrated in her column, by choosing to switch doors, you will win the million doors 66.66% of the time. I hope that you enjoyed reading this!
