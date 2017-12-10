from Coach import Coach
from OthelloGame import OthelloGame
from NNet import NNetWrapper as nn
from utils import *

args = dotdict({
    'numIters': 1000,
    'numEps': 100,
    'tempThreshold': 25,
    'updateThreshold': 0.6,
    'maxlenOfQueue': 200000,
    'numMCTSSims': 50,
    'arenaCompare': 40,
    'cpuct': 1,

    'checkpoint': '/dev/models/8x100x50_cont/',
    'load_model': True,
    'load_folder_file': ('/dev/models/8x100x50','best.pth.tar'),
})

if __name__=="__main__":
    g = OthelloGame(8)
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])
        
    c = Coach(g, nnet, args)
    c.learn()
