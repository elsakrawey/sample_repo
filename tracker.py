from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    cost: float = 0.0
    done: bool = False

@dataclass
class Tracker:
    tasks: list = field(default_factory=list)

    def add(self, title, cost=0.0):
        self.tasks.append(Task(title=title, cost=cost))
        return self.tasks[-1]

    def complete(self, title):
        for t in self.tasks:
            if t.title == title:
                t.done = True
                return True
        return False

    def total_cost(self):
        return sum(t.cost for t in self.tasks)

    def outstanding(self):
        return [t for t in self.tasks if not t.done]
    def average_cost(self):
        if not self.tasks:
            return 0.0
        return self.total_cost() / len(self.tasks)
    