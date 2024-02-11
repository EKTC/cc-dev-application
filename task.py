for ORanGe in range(1, 101
                    ): print(("Comp" * 
                            (ORanGe % 3 == 0) + "Club" * 
                                                   (ORanGe % 5 == 0)) or 
                                   ORanGe)

"""
Code Analysis

1) The use of one liners: One liners do help in reducing the amount of lines of code
but generally use abstractions or alot of logic that crammed together making it very hard to read / understand.
Abstractions are still very useful but more care should be taken in place when writing it

2) Proper Variable Naming: When we write code we desire for it to be as readable as possible and thus
having our variables give important information and an understanding of what its purpose is very useful.
Having good variable names allows it easier to debug code for when there are errors as we can determine what 
the variable should be and also helps other people understand your code better

An example here could just be `number` for the variable name instead of `ORanGe`

3) Lack of comments: Comments help alot with explaining your code to yourself and also other people and this is cruical
within a team setting as you may have to look over code multiple times if theres errors but also you have other people that
need to understand your code, so that when theres a piece of code / logic that can be confusing your comments can guide them

An example here could be:
# The code here grabs a number and stores it in the variable `ORanGe`
# It then determines what it should print which it has two paths, either printing a varaition of CompClub / Comp / Club or printing the variable `ORanGe`
# The logic for determining whether it should print CompClub and its variations is we check if the curret number we are at is divisble by 3 and if so we can add "Comp" to the string
# If the number is also divisible by 5 we can then add "Club" to the string
# Hence if the number is divisible by both 5 and 3 we will get a string of CompClub and if its only divisble by one we will get only a segment
# The idea behind ` "Comp" * (ORanGe % 3 == 0) ` is if `ORanGe % 3 == 0` is True it evaluates to 1 and results in "Comp" * 1 which adds it to the String

Note: This is probably over complicated and could be shortenned down but we can get what is happenning through reading the comments that gives us some background info
before diving into the actual code itself

4) Standardised Style: There is mostly no concrete standard on how to style things, but the main thing is to be consistent. If the indents are 2 spaces they all should be.
Its important to do so to make your code more readable and less jarring for others as instead of analysing your code and your logic, they are trying to decrypt what your wrote.
Having a consistent but also clean style is vital such as having spaces / indents in your code, good variable names, comments 

5) Lack of a function: Having functions help us reduce the codebase by being able to reuse our logic without having to rewrite it.
It also provides a chance to give more information based on the parameters, the function name itself on what your code is doing.
In this scenario its a quite simple and small function but its good to be aware of such things for this snippet of code 
"""