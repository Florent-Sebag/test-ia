from search import Problem

class Game(Problem):
    def __init__(self, init, goal):
        Problem.__init__(self, init, goal)
        self.count = 0

    def actions(self, state, is_on_ret=False):
        if (is_on_ret):
            self.initial[0] -= 1
        else:
            if (state != 0):
                self.initial[0] += 1
            self.initial[state] += 1

    def state_to_str(self, pos):
        if (pos == 0):
            return ("Left")
        if (pos == 1):
            return ("Center")
        return ("Right")

    def print_game(self):
        print("-----------TURN " + str(self.count) + "-----------")
        print("Hombre : " + self.state_to_str(self.initial[0]) + ", " +\
        "Lobo : " + self.state_to_str(self.initial[1]) + ", " + \
        "Col : " + self.state_to_str(self.initial[2]) + ", " + \
        "Cabra : " + self.state_to_str(self.initial[3]) + "\n")
        self.count += 1



class IA():
    def __init__(self, z):
        self.is_on_ret = False
        self.actual_state = 0
        self.game = z


    def letsPlay(self):
        self.game.print_game()

        while (not self.game.goal_test(self.game.initial)):
            if (self.game.initial[0] == 0):
                self.is_on_ret = False
                self.actual_state += 1
                self.game.actions(self.actual_state)

            elif (self.game.initial[0] == 1 and not self.is_on_ret):
                self.game.actions(self.actual_state)

            else:
                self.is_on_ret = True
                self.game.actions(0, self.is_on_ret)

            self.game.print_game()

        print("Done")


players = [0, 0, 0, 0]
goal = [2, 2, 2, 2]

z = Game(players, goal)
ia = IA(z)

ia.letsPlay()
