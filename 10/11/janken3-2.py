import random

# じゃんけんの手の名前を対応付け
hands = {0: "グー", 1: "チョキ", 2: "パー"}

# 勝敗判定の関数（3人の場合）
def judge_three(a, b, c):
    # すべての手が同じなら引き分け
    if a == b == c:
        return "引き分け"
    
    #二人が同時に勝つ場合
    if(a==b):
        if(a == 0 and c == 1) or (a == 1 and c == 2) or (a == 2 and c == 0):
            return "AとBの勝ち"
    if(a==c):
        if(a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
            return "AとCの勝ち"
    if(b==c):
        if(b == 0 and a == 1) or (b == 1 and a == 2) or (b == 2 and a == 0):
            return "AとCの勝ち"
    
     # Aが勝つ場合
    if (a == 0 and b == 1 and c == 1) or (a == 1 and b == 2 and c == 2) or (a == 2 and b == 0 and c == 0):
        return "Aの勝ち"
    # Bが勝つ場合
    elif (b == 0 and a == 1 and c == 1) or (b == 1 and a == 2 and c == 2) or (b == 2 and a == 0 and c == 0):
        return "Bの勝ち"
    # Cが勝つ場合
    elif (c == 0 and a == 1 and b == 1) or (c == 1 and a == 2 and b == 2) or (c == 2 and a == 0 and b == 0):
        return "Cの勝ち"
    else:
        return "引き分け"

# じゃんけんの1回分のシミュレーション
def janken_round():
    # A, B, Cの手をランダムに生成
    a_hand = random.randint(0, 2)
    b_hand = random.randint(0, 2)
    c_hand = random.randint(0, 2)
    
    # 手の名前を取得
    a_hand_name = hands[a_hand]
    b_hand_name = hands[b_hand]
    c_hand_name = hands[c_hand]
    
    # 勝敗判定
    result = judge_three(a_hand, b_hand, c_hand)
    
    # 結果を出力
    print(f"Aの手: {a_hand_name}, Bの手: {b_hand_name}, Cの手: {c_hand_name} → {result}")
    
    return result

# じゃんけん三回勝負の関数（同時に勝った場合も考慮）
def janken_best_of_three():
    a_wins = 0
    b_wins = 0
    c_wins = 0
    rounds = 0
    
    while True:
        result = janken_round()
        rounds += 1
        
        if "A" in result:
            a_wins += 1
        if "B" in result:
            b_wins += 1
        if "C" in result:
            c_wins += 1
        
        print(f"現在のスコア: A {a_wins} - B {b_wins} - C {c_wins}\n")
        
        # 2人または3人が3勝に到達した場合、勝者が1人多く勝つまで続行
        if (a_wins >= 3 and b_wins >= 3) or (a_wins >= 3 and c_wins >= 3) or (b_wins >= 3 and c_wins >= 3):
            print("2人以上が3勝しました。勝者が1人多く勝つまで続行します。\n")
        # 1人だけが3勝した場合、終了
        elif (a_wins == 3 and b_wins < 3 and c_wins < 3) or (b_wins == 3 and a_wins < 3 and c_wins < 3) or (c_wins == 3 and a_wins < 3 and b_wins < 3):
            break
    
    # 最終結果を出力
    if a_wins > b_wins and a_wins > c_wins:
        print(f"結果: Aが{rounds}回のじゃんけんで勝ちました！")
    elif b_wins > a_wins and b_wins > c_wins:
        print(f"結果: Bが{rounds}回のじゃんけんで勝ちました！")
    elif c_wins > a_wins and c_wins > b_wins:
        print(f"結果: Cが{rounds}回のじゃんけんで勝ちました！")
    else:
        print("勝者が決まりませんでした。")

# 三回勝負を実行
janken_best_of_three()
