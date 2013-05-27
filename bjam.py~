from codejam.utils.codejamrunner import CodeJamRunner
import codejam.utils.graphing as graphing
import networkx as nx

class Dynam(object):pass

def find_max_act_eff(start, end, index, length, data):

        pre_limit = min(data.max_e, start + index * data.regain)
        post_limit  = max(0, end - ((length - index) * data.regain))
        activity_effort = pre_limit - post_limit

        return activity_effort, pre_limit, post_limit
    

def solver(data):

    gain = 0
    segments = []
    #                Start val, end val,     segment values
    segments.append((data.max_e, data.regain, data.activity_vals))

    while segments:
        seg = segments.pop()

        activities = seg[2]
        hi_pri = max(activities)
        ind = activities.index(hi_pri)

        # add the new gain
        eff, pre, post = find_max_act_eff(seg[0], seg[1], ind, len(activities), data)        
        seg_gain = eff * hi_pri
        gain += seg_gain

        # append the pre_segment for processing
        pre_seg= activities[:ind]
        pre_st = seg[0]
        pre_fin = pre
        if len(pre_seg) > 0 and len(pre_seg) * data.regain > pre_st - pre_fin:
            segments.append((pre_st, pre_fin, pre_seg))

        # append the post segment for processing
        post_seg = activities[ind+1:]
        post_st = post + data.regain
        post_fin = seg[1]
        if len(post_seg) > 0 and len(post_seg) * data.regain > post_st - post_fin:
            segments.append((post_st, post_fin, post_seg))




        
    return gain

  
def data_builder(f):

    data = Dynam()
    data.max_e, data.regain, data.activity_count = f.get_ints()
    data.activity_vals = f.get_ints()

    return data



cjr = CodeJamRunner()
cjr.run(data_builder, solver, problem_name = "B", problem_size='large-practice')
