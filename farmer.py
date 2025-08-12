from experta import *


class Wolf:
    def __init__(self):
        self.position = 0  # 0:  start, 1 : end


class Farmer:
    def __init__(self):
        self.position = 0


class Cabbage:
    def __init__(self):
        self.position = 0


class Goat:
    def __init__(self):
        self.position = 0


class State(Fact):
    def __init__(self, wolf, goat, cabbage, farmer):
        self.wolf = wolf
        self.goat = goat
        self.cabbage = cabbage
        self.farmer = farmer


class RiverCrossing(KnowledgeEngine):
    def __init__(self):
        self.steps = []

    @DefFacts()
    def initial_state(self):
        yield State(wolf=Wolf(), goat=Goat(), cabbage=Cabbage(), farmer=Farmer())

    @Rule(State(wolf=MATCH.wolf, goat=MATCH.goat, cabbage=MATCH.cabbage, farmer=MATCH.farmer))
    def yield_wolf(self, wolf):
        yield wolf.position

    @Rule(State(wolf=MATCH.wolf, goat=MATCH.goat, cabbage=MATCH.cabbage, farmer=MATCH.farmer))
    def yield_goat(self, goat):
        yield goat.position

    @Rule(State(wolf=MATCH.wolf, goat=MATCH.goat, cabbage=MATCH.cabbage, farmer=MATCH.farmer))
    def yield_cabbage(self, cabbage):
        yield cabbage.position

    @Rule(State(wolf=MATCH.wolf, goat=MATCH.goat, cabbage=MATCH.cabbage, farmer=MATCH.farmer))
    def yield_farmer(self, farmer):
        yield farmer.position

    @Rule(State(wolf=1, goat=1, cabbage=1, farmer=1))
    def goal_state(self):
        print("Done: Wolf, goat, cabbage, and farmer are moved.")
        print("Solution steps:")
        for step in self.steps:
            print(step)

    @Rule(State(wolf=MATCH.wolf, goat=MATCH.goat, cabbage=MATCH.cabbage, farmer=MATCH.farmer) &
          ((MATCH.wolf == MATCH.goat) & (MATCH.farmer != MATCH.goat)) | ((MATCH.goat == MATCH.cabbage) & (MATCH.farmer != MATCH.goat)))
    def invalid_state(self):
        print("Invalid state: Wolf will eat the goat or goat will eat the cabbage.")
        self.deactivate()

    @Rule(State(wolf=MATCH.wolf, goat=MATCH.goat, cabbage=MATCH.cabbage, farmer=MATCH.farmer) & (MATCH.farmer == 1))
    def move_farmer(self):
        new_state = State(wolf=self.facts[0].wolf, goat=self.facts[0].goat,
                          cabbage=self.facts[0].cabbage, farmer=1 - self.facts[0].farmer)
        self.steps.append(new_state)
        self.declare(new_state)

    @Rule(State(wolf=MATCH.wolf, goat=MATCH.goat, cabbage=MATCH.cabbage, farmer=MATCH.farmer) & (MATCH.farmer == 1))
    def move_wolf(self):
        new_state = State(wolf=1 - self.facts[0].wolf, goat=self.facts[0].goat,
                          cabbage=self.facts[0].cabbage, farmer=1 - self.facts[0].farmer)
        self.steps.append(new_state)
        self.declare(new_state)

    @Rule(State(wolf=MATCH.wolf, goat=MATCH.goat, cabbage=MATCH.cabbage, farmer=MATCH.farmer) & (MATCH.farmer == 1))
    def move_goat(self):
        new_state = State(wolf=self.facts[0].wolf, goat=1 - self.facts[0].goat,
                          cabbage=self.facts[0].cabbage, farmer=1 - self.facts[0].farmer)
        self.steps.append(new_state)
        self.declare(new_state)

    @Rule(State(wolf=MATCH.wolf, goat=MATCH.goat, cabbage=MATCH.cabbage, farmer=MATCH.farmer) & (MATCH.farmer == 1))
    def move_cabbage(self):
        new_state = State(wolf=self.facts[0].wolf, goat=self.facts[0].goat,
                          cabbage=1 - self.facts[0].cabbage, farmer=1 - self.facts[0].farmer)
        self.steps.append(new_state)
        self.declare(new_state)


if __name__ == "__main__":

    engine = RiverCrossing()
    engine.reset()

    queue = list([engine.facts[0]])
    visited = set()

    while queue:
        state = queue.pop(0)
        if state in visited:
            continue

        engine.facts = [state]
        engine.run()

        if engine.is_halted:
            break

        visited.add(state)

        for fact in engine.facts:
            queue.append(fact)

    print("Visited states of the solution:")
    for state in visited:
        print(state)
