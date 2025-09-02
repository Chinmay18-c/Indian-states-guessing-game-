import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian State & union territory game")
image = "inde15.gif"
screen.addshape(image)
screen.setup(width=870, height=850)

turtle.shape(image)

data = pandas.read_csv("37_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states) }/{ len(all_states)} States Correct",
                                    prompt="What's another State name?")

    if not answer_state:
        break

    answer_state=answer_state.title()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        state_coordinate=data[data.state==answer_state]
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        x=float(state_coordinate.x)
        y=float(state_coordinate.y)
        t.goto(x,y)
        t.write(answer_state)

Missing_states=[]
for state in all_states:
    if state not in guessed_states:
        Missing_states.append(state)
df=pandas.DataFrame(Missing_states)
df.to_csv("states_to_learn.csv")
turtle.mainloop()
