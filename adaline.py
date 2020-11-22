def train_model():
    inputs =  [[1, 1, 1],
 [1, 1, -1],
 [1, -1, 1],
 [1, -1, -1],
 [-1, 1, 1],
 [-1, 1, -1],
 [-1, -1, 1],
 [-1, -1, -1]]
    
    weights = [0,0,0]
    targets = [1, -1, 1, -1,  1, -1, 1, 1]
    bias = 0
    alpha = 0.1
    summ = 0
    predicted_output = 0
    desired_output = 0
    count = 0

    for i in range(0,len(targets)):
        for j in range(0,len(targets)):
            count+=1
            list1 = []
            hx = vector_multiplication(inputs[j],weights)+bias

            if hx<0:
                predicted_output = -1
            else:
                predicted_output = 1
           
            if predicted_output == targets[j]:
                pass
            else:
                bias = bias+(alpha*(targets[j]-hx))
                print("INPUTS "+str(inputs[j]))

                for i in range(0,len(inputs[0])):
                    list1.append(weights[i]+(alpha*(targets[j]-hx)*inputs[j][i]))
                weights = list1
                
    print("== Trained Model ==\nBIAS  " + str(bias) +"  Weights  " + str(weights))
    output_list = [bias,weights]
    return output_list

def test_model(test_outputs):
    print("== Testing Model ==")
    vector_size = len(test_outputs[1])
    inputs = []
    for i in range(0,vector_size):
        v1 = float (input("Enter test input value "+str(i+1)+":  " ))
        inputs.append(v1)
    bias = test_outputs[0]
    hx = vector_multiplication(inputs,test_outputs[1])+bias
    if hx<0:
        output_value = -1
    else:
        output_value = 1
    print("Output is "+str(output_value))
    return output_value

def vector_multiplication(vector1,vector2):
    summ = 0
    if(len(vector1)!=len(vector2)):
        print("ERROR : Given vectors cannot be multiplied!")

    else:
        for i in range(len(vector1)):
            summ = summ + vector1[i]*vector2[i]
    return summ
        
if __name__ == "__main__":
    outputs = train_model()
    test_model(outputs)
    

