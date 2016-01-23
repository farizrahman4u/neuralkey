# neuralkey
Neural Key Exchange using Tree Parity Machine in Python

**Hi!** This is an implementaion of the Neural Key Exchange Protocol in python written with simplicity, understandability and code readability in mind. Suiltable for academic and researh purposes. The code is documented line by line, so lets get straight to theory.
___
**Diffie–Hellman key exchange**

If Alice and Bob wish to communicate with each other by exchanging encrypted messages, each of them should be able to decrypt the messages received from the other. And to do so, they have to exchange the keys with which the messages will be encrypted, and should be carefull not to let Eve get hold of the keys, or else she too would be able to decrypt the messages. So a secure protocol should be used for exchanging the keys, or else nosy Eve would be able to read all of Bob's and Alice's messages.
Neural or not, the most used protocol for key exchange between two parties A and B is the [Diffie-Hellman protocol](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange). Diffie–Hellman Key Exchange establishes a shared secret between two parties that can be used for secret communication for exchanging data over a public network. The following conceptual diagram illustrates the general idea of the key exchange by using colors instead of very large numbers:

![Diffe-Hellman](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Diffie-Hellman_Key_Exchange.svg/250px-Diffie-Hellman_Key_Exchange.svg.png)
____
**Neural Key Exchange Protocol**

The Diffe-Hellman protocol can be implemented using a neural neural network with a single hidden layer (also called a tree parity machine). The number neurons in the hidden layer is denoted as `K` and the number of input neurons per hidden neuron is denoted as 'N'. There is a weight matrix `W` between the input and hidden layers of dimensions `K`x`N` and the range of each weight is `{-L, ..., -2, -1, 0, 1, 2, ..., +L}` where `L` is a parameter of the tree.

![tpm](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/TreeParityMachine.jpg/350px-TreeParityMachine.jpg)

Both Bob and Alice posses tree parity machines with same set of parameters (`K`, `N` and `L`). The weights of their machines are different, as they are randomly initialized. If they could synchronize the weights of their machines (without transferring the actual weights, ofcourse) they could then use those weights as a cryptographic key for the rest of their communication. The following algorithm is used to synchronize the weight matrices of Bob's and Alice's machines:

![algorith](http://i66.tinypic.com/rk0jd5.png)

For a given random input vector x (of dimensions [`K`,`N`]), the output (tau) of a tree parity machine is computed as follows:

![eqn1](https://upload.wikimedia.org/math/3/7/8/378239a5ebfd6a4909c41bfb56290785.png)

![eqn2](https://upload.wikimedia.org/math/f/0/c/f0cc1ef36d3e0ed3122a4d5bb5174b24.png)

![eqn2](https://upload.wikimedia.org/math/f/6/c/f6c71d6ddb62c05156e28257d2ee7321.png)

![eqn3](https://upload.wikimedia.org/math/2/6/c/26ca3289b0a374f571997861520afd19.png)

![eqn4](https://upload.wikimedia.org/math/8/e/2/8e294fb8aa31d991f17adb60962a35ba.png)

And if the outputs of both Alice's and Bob's machines are equal, their weights are update using any of the following rules:

* Hebbian rule:

![hebbian](https://upload.wikimedia.org/math/e/a/0/ea00bf9f38c084eb3dd2f05f18d7c7f8.png)

* Anti-hebbian rule:

![anti-hebbian](https://upload.wikimedia.org/math/4/b/e/4be8643c90715a90d50f1699dcccffb5.png)

* Random-walk:

![random-walk](https://upload.wikimedia.org/math/2/7/4/274044e2c0b5f84e79f7080270a4d48d.png)
___

# The Code

The code is heavily documented. It consists of 3 files, `machine.py`, which defines a tree parity machine, `update_rules.py`, which contains functions for all the three update rules and `run.py` which simple creates 2 machines with default parameters and try to sync them.

**Installation**

```
sudo git clone http://www.github.com/farizrahman4u/neuralkey.git
cd neuralkey
python run.py
```

**Requirements**
* [Numpy](www.numpy.org)
* [Matplotlib](www.matplotlib.org)

**TODO**

* Simulate Eve and man in the middle attack
* Improve visualization

___

#Bye!!
