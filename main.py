import pandas as pd
import json
def main():
    csv_data = pd.read_csv("./data/APO_Familytree.csv")



    node_list = []
    node_children_list = []
    for i in range(len(csv_data)):
        data_point = {"id": str(csv_data.iloc[i]["ID"]),"name": csv_data.iloc[i]["Name"],"house": csv_data.iloc[i]["House"]}
        node_list.append(data_point)

        data_point = {"name": csv_data.iloc[i]["Name"],
                      "house": csv_data.iloc[i]["House"], "children": []}

        node_children_list.append(data_point)

    print(node_list)


    edge_list = []

    for j in range(len(csv_data)):
        big_id = None

        for k in node_list:
            if k["name"] == csv_data.iloc[j]["Big1"]:
                big_id = k["id"]
                break
        if big_id is not None:
            #From big point to little
            data_point = {"source": big_id, "target": str(csv_data.iloc[j]["ID"])}
            edge_list.append(data_point)

            #check for second big
            if type(csv_data.iloc[j]["Big2"]) != float:
                big2_id = None

                #search for second big
                for k in node_list:
                    if k["name"] == csv_data.iloc[j]["Big2"]:
                        big2_id = k["id"]
                        break
                if big2_id is not None:
                    data_point = {"source": big2_id, "target":  str(csv_data.iloc[j]["ID"])}
                    edge_list.append(data_point)


    print(edge_list)

    # # for each node get its bigs
    # for j in range(len(csv_data)):
    #     big_id = None
    #
    #     current_node = csv_data.iloc[j]
    #     current_node_big = csv_data.iloc[j]["Big1"]
    #
    #     for k in node_children_list:
    #         if k["name"] == current_node_big:
    #             big_id = k
    #             break
    #     if big_id is not None:
    #         big_id["children"].append(current_node)
    #
    #         print(big_id["children"])
    #
    #         # check for second big
    #         if type(csv_data.iloc[j]["Big2"]) != float:
    #             big2_id = None
    #
    #             # search for second big
    #             for k in node_children_list:
    #                 if k["name"] == csv_data.iloc[j]["Big2"]:
    #                     big2_id = k
    #                     break
    #             if big2_id is not None:
    #                 big2_id["children"].append(current_node)
    #

    full_data = {"nodes": node_list,"edges":edge_list}

    with open('./data/phi_nodes.json', 'w') as outfile:
        json.dump(node_list, outfile)
    with open('./data/phi_edges.json', 'w') as outfile:
        json.dump(edge_list, outfile)
    with open('./data/phi_fulldata.json', 'w') as outfile:
        json.dump(full_data, outfile)
    # with open('./data/phi_childrendata.json', 'w') as outfile:
    #     json.dump(node_children_list, outfile)

if __name__ == "__main__":
    main()