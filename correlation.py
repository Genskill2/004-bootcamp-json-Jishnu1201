import json
import math

# Add the functions in this file
def load_journal(filename):#returns parsed data from journal.json
    f= open(filename)
    r = f.read()
    f.close()
    data = json.loads(r)
    return data

#returns phi value
def compute_phi(filename, event):
    data = load_journal(filename)
    n = [0,0,0,0,0,0,0,0]
    for day in data:
        if event in day['events']:
            if day['squirrel']:
                n[0] += 1
            else:
                n[2] += 1
        
        else:
            if day['squirrel']:
                n[3] += 1
            else:
                n[1] += 1
    
    n[4] = n[0] + n[2]
    n[5] = n[1] + n[3]
    n[6] = n[0] + n[3]
    n[7] = n[1] + n[2]

    phi = (n[0] * n[1] - n[2] * n[3]) / math.sqrt(n[4] * n[5] * n[6] * n[7])
    return phi

#returns dictionary of phi values pf all distinct events
def compute_correlations(filename):
    data = load_journal(filename)
    corr = {}
    for day in data:
        for event in day['events']:
            if event not in corr:
                corr[event] = compute_phi(filename, event)
    return corr

#returns highest and least correlated values
def diagnose(filename):
    corr = compute_correlations(filename)
    max_val = max(corr, key = corr.get)
    min_val = min(corr, key = corr.get)
    return max_val, min_val
