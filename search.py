# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # ss = problem.getStartState()
    # visited = []
    # queue = []
    # queue.append(ss)
    # return dfs_Util(problem,visited,queue)
    # t = problem.getSuccessors(s)
    # print t
    # # print problem.getSuccessors(t[0][0])
    # # print t[0][0][1]
    # if t:
    #     print t[::-1]
    # l = []
    # print problem.getSuccessors(t[0])
    # l.append(s)
    # while not l:
    #     s = l.pop()
    ss = problem.getStartState()
    st = util.Stack()
    path = []
    visited = []
    st.push([ss,path,0])
    while not st.isEmpty():
        node = st.pop()
        if node[0] not in visited:
            visited.append(node[0])
            if problem.isGoalState(node[0]):
                return node[1]
            succ = problem.getSuccessors(node[0])
            if succ:
                for next_n in succ:
                    st.push([next_n[0],node[1]+[next_n[1]],next_n[2]])
    util.raiseNotDefined()

# def dfs_Util(problem,visited,queue):
#     nn = queue.pop()
#     if problem.isGoalState(nn):
#         return []
#     visited.append(nn)
#     next_n = problem.getSuccessors(nn)
#     print next_n
#     # next_n = next_n.reverse()
#     for node in next_n:
#         if node[0] not in visited:
#             queue.append(node[0])
#             res = dfs_Util(problem,visited,queue)
#             if res is not None:
#                 res.insert(0,node[1])
#                 return res

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    ss = problem.getStartState()
    st = util.Queue()
    path = []
    visited = [ss[0]]
    st.push([ss,path,0])
    while not st.isEmpty():
        node = st.pop()
        state = node[0]
        if problem.isGoalState(state):
            return node[1]
        succ = problem.getSuccessors(state)
        if succ:
            for next_n in succ:
                if next_n[0] not in visited:
                    visited.append(next_n[0])
                    st.push([next_n[0],node[1]+[next_n[1]],next_n[2]])
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ss = problem.getStartState()
    queue = util.PriorityQueue()
    path = []
    visited = []
    queue.push([ss,path,0],0)
    while not queue.isEmpty():
        node = queue.pop()
        if node[0] not in visited:
            visited.append(node[0])
            if problem.isGoalState(node[0]):
                return node[1]
            succ = problem.getSuccessors(node[0])
            if succ:
                for next_n in succ:
                    tc = next_n[2] + node[2]
                    queue.push([next_n[0],node[1]+[next_n[1]],tc],tc)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    ss = problem.getStartState()
    queue = util.PriorityQueue()
    path = []
    visited = []
    cost_so_far = [[ss,0]]
    queue.push([ss,path,0],0+heuristic(ss,problem))
    while not queue.isEmpty():
        node = queue.pop()
        if node[0] not in visited:
            visited.append(node[0])
            if problem.isGoalState(node[0]):
                return node[1]
            succ = problem.getSuccessors(node[0])
            
            if succ:
                for next_n in succ:
                    next_CA=0
                    for lst in cost_so_far:
                        if(lst[0] == node[0]):
                            cost_so_far_node0 = lst[1]
                        if(lst[0] == next_n[0]):
                            next_CA = 1
                            cost_so_far_next = lst[1]
                    tc = next_n[2] + cost_so_far_node0
                    wl = [next_n[0],tc]
                    if next_CA == 0:
                        cost_so_far.append(wl)
                        queue.push([next_n[0],node[1]+[next_n[1]],tc+heuristic(next_n[0],problem)],tc+heuristic(next_n[0],problem))
                    if next_CA == 1:
                        if tc < cost_so_far_next:
                            for lst in cost_so_far:
                                if(lst[0] == next_n[0]):
                                    lst[1] = tc
                            queue.push([next_n[0],node[1]+[next_n[1]],tc+heuristic(next_n[0],problem)],tc+heuristic(next_n[0],problem))
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
