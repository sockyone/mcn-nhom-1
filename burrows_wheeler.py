EOS = "$"
import sys
import sufarray

def calc_first_occ(s):
    A = {}
    for i, c in enumerate(s):
        if A.get(c):
            A[c] += 1
        else:
            A[c] = 1
    
    # sort the letters
    letters = sorted(A.keys())
    
    # first index of letter
    occ = {}
    
    idx = 0
    for c in letters:
        occ[c] = idx
        idx += A[c]
    del idx, A

    print(occ)
    # {'$': 0, 'a': 1, 'b': 4, 'n': 5}

    return occ

def inverse(s):
        occ = calc_first_occ(s)
        
        lf = [0] * len(s)
        for i, c in enumerate(s):
            lf[i] = occ[c]
            occ[c] += 1
        del occ

        print(lf)
        # [1, 5, 6, 4, 0, 2, 3]
        
        r = ['']*(len(s)-1)
        i = 0
        
        for k in range(len(r)-1,-1,-1):
            r[k] = s[i]
            i = lf[i]
            
        r = ''.join(r)
        return r.rstrip(EOS)

def transform(s):
        assert EOS not in s, "Input string cannot contain null character (%s)" % EOS
        
        # add end of text marker
        s += EOS
        
        # table of suffixes
        
        sarray = sufarray.SufArray(s)

        rotations = sarray.get_array()
        
        # get the length of ordered suffixes
        k = len(rotations)
        
        r = [0]*k
        for i in range(k):
            r[i] = s[(rotations[i] + k - 1)%k]
        r = ''.join(r)
        
        return r

if __name__ == "__main__":
    mode = sys.argv[1]
    input_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    if mode == "e":
        # encode
        f = open(input_file_path, "r")
        text = f.read()
        f2 = open(output_file_path, "w")
        # print("Start transform")
        f2.write(transform(text))
        

    elif mode == "d":
        f = open(input_file_path, "r")
        text = f.read()
        f2 = open(output_file_path, "w")
        f2.write(inverse(text))