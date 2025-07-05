import numpy as np

def calculate(list):
    
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    
    
    listReshape= np.array(list).reshape(3,3)
 
 
    calculations  ={ 
        'mean':[listReshape.mean(axis=0).tolist(), 
                listReshape.mean(axis=1).tolist(), 
                listReshape.mean().item()],
        'variance': [listReshape.var(axis=0).tolist()
                     , listReshape.var(axis=1).tolist(), 
                     listReshape.var().item()],
        'standard deviation':[listReshape.std(axis=0).tolist(), 
                              listReshape.std(axis=1).tolist(), listReshape.std().item()],
        'max': [listReshape.max(axis=0).tolist(),
                listReshape.max(axis=1).tolist(), 
                listReshape.max().item()],
        'min' : [listReshape.min(axis=0).tolist(), 
                 listReshape.min(axis=1).tolist(),
                 listReshape.min().item()]}


    return calculations