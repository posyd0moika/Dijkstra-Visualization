from collections import deque


class CreateData:
    def __init__(self):
        self.G = {}

    def __call__(self, p1, p2):
        if self.G.get(p1, False) is False:
            self.G[p1] = {}

        if self.G.get(p2, False) is False:
            self.G[p2] = {}

        self.G[p2][p1] = 1
        self.G[p1][p2] = 1


class Dijkstra:
    def __init__(self, G, start):
        self.G = G
        self.Gm = {k: None for k in self.G}
        self.Gm[start] = 0
        self.drque = deque([start])
        self.start = start

    def start_algorithm(self):
        while self.drque:
            point = self.drque.popleft()
            for key, value in self.G[point].items():
                if self.Gm[key] is None:
                    self.Gm[key] = value + self.Gm[point]
                    self.drque.append(key)
                elif self.Gm[key] + value < self.Gm[point]:
                    self.Gm[point] = self.Gm[key] + value
                    self.drque.append(point)
                elif self.Gm[key] > self.Gm[point] + value:
                    self.Gm[key] = self.Gm[point] + value
                    self.drque.append(key)

    def start_finish(self, finish, stak=...):
        stak = [] if stak is ... else stak[:]
        stak.append(finish)
        if self.start == finish:
            return stak
        if finish in self.G:
            for key, value in self.G[finish].items():
                try:
                    if self.Gm[finish] - value == self.Gm[key]:
                        return self.start_finish(key, stak)
                except:
                    pass

    @staticmethod
    def dijkstra_gen(G, start, finish):
        for point in start:
            dijkstra = Dijkstra(G, point)
            try:
                dijkstra.start_algorithm()
            except KeyError:
                for fin in finish:
                    yield point, fin, []
                continue

            for fin in finish:
                stak = dijkstra.start_finish(fin)
                if stak is None:
                    continue
                yield point, fin, stak
