# -*- coding:utf-8 -*-

import torch
torch.manual_seed(1)

# ======================================= example 1 =======================================
# torch.cat
# 将多个张量沿指定维度堆叠在一起
# flag = True
flag = False

if flag:
    t = torch.ones((2, 3))  # 创建一个两行三列的全1张量
    t_0 = torch.cat([t, t], dim=0)  # 创建一个(4,3)的全一张量
    t_1 = torch.cat([t, t, t], dim=1)  # 创建一个(2,9)的全一张量

    print("t_0:{} shape:{}\nt_1:{} shape:{}".format(
        t_0, t_0.shape, t_1, t_1.shape))


# ======================================= example 2 =======================================
# torch.stack
# 在新的维度堆叠多个张量
flag = True
# flag = False

if flag:
    t = torch.ones((2, 3))

    t_stack = torch.stack([t, t, t], dim=1)

    print("\nt_stack:{} shape:{}".format(t_stack, t_stack.shape))


# 当 torch.stack 在某个维度上创建新的维度时，新维度的大小通常等于堆叠的张量数量，而不是原始维度的大小。这是因为 torch.stack 的目的是在新维度上堆叠不同的张量，以保持它们的顺序和一致性。

# 具体来说：

# 当 dim=0 时，你要将多个张量按顺序堆叠在一起，因此新维度的大小必须等于堆叠的张量数量，以容纳所有的张量。

# 当 dim=1 时，你要在原始维度1上堆叠，为了保持堆叠的张量在这个维度上具有相同的大小，新维度的大小必须等于堆叠的张量数量。

# 当 dim=2 时，你同样要将多个张量按顺序堆叠在维度2上，因此新维度的大小等于堆叠的张量数量。
# ======================================= example 3 =======================================
# torch.chunk

# flag = True
flag = False

if flag:
    a = torch.ones((2, 7))  # 7
    list_of_tensors = torch.chunk(a, dim=1, chunks=3)   # 3

    for idx, t in enumerate(list_of_tensors):
        print("第{}个张量：{}, shape is {}".format(idx+1, t, t.shape))


# ======================================= example 4 =======================================
# torch.split

# flag = True
flag = False

if flag:
    t = torch.ones((2, 5))

    list_of_tensors = torch.split(t, [2, 1, 1], dim=1)  # [2 , 1, 2]
    for idx, t in enumerate(list_of_tensors):
        print("第{}个张量：{}, shape is {}".format(idx+1, t, t.shape))

    # list_of_tensors = torch.split(t, [2, 1, 2], dim=1)
    # for idx, t in enumerate(list_of_tensors):
    #     print("第{}个张量：{}, shape is {}".format(idx, t, t.shape))


# ======================================= example 5 =======================================
# torch.index_select

# flag = True
flag = False

if flag:
    t = torch.randint(0, 9, size=(3, 3))
    idx = torch.tensor([0, 2], dtype=torch.long)    # float
    t_select = torch.index_select(t, dim=0, index=idx)
    print("t:\n{}\nt_select:\n{}".format(t, t_select))

# ======================================= example 6 =======================================
# torch.masked_select

# flag = True
flag = False

if flag:

    t = torch.randint(0, 9, size=(3, 3))
    # ge is mean greater than or equal/   gt: greater than  le  lt
    mask = t.le(5)
    t_select = torch.masked_select(t, mask)
    print("t:\n{}\nmask:\n{}\nt_select:\n{} ".format(t, mask, t_select))


# ======================================= example 7 =======================================
# torch.reshape

# flag = True
flag = False

if flag:
    t = torch.randperm(8)
    t_reshape = torch.reshape(t, (-1, 2, 2))    # -1
    print("t:{}\nt_reshape:\n{}".format(t, t_reshape))

    t[0] = 1024
    print("t:{}\nt_reshape:\n{}".format(t, t_reshape))
    print("t.data 内存地址:{}".format(id(t.data)))
    print("t_reshape.data 内存地址:{}".format(id(t_reshape.data)))


# ======================================= example 8 =======================================
# torch.transpose

# flag = True
flag = False

if flag:
    # torch.transpose
    t = torch.rand((2, 3, 4))
    t_transpose = torch.transpose(t, dim0=1, dim1=2)    # c*h*w     h*w*c
    print("t shape:{}\nt_transpose shape: {}".format(t.shape, t_transpose.shape))


# ======================================= example 9 =======================================
# torch.squeeze

# flag = True
flag = False

if flag:
    t = torch.rand((1, 2, 3, 1))
    t_sq = torch.squeeze(t)
    t_0 = torch.squeeze(t, dim=0)
    t_1 = torch.squeeze(t, dim=1)
    print(t.shape)
    print(t_sq.shape)
    print(t_0.shape)
    print(t_1.shape)


# ======================================= example 8 =======================================
# torch.add

# flag = True
flag = False

if flag:
    t_0 = torch.randn((3, 3))
    t_1 = torch.ones_like(t_0)
    t_add = torch.add(t_0, 10, t_1)

    print("t_0:\n{}\nt_1:\n{}\nt_add_10:\n{}".format(t_0, t_1, t_add))
