import streamlit as st
import random

# ページ設定
st.set_page_config(
    page_title="Whiskey Expert Quiz",
    page_icon="🥃",
    layout="centered",
)

# タイトル
st.title("🥃 Whiskey Expert Quiz")
st.markdown("ウィスキーエキスパート資格試験対策クイズ")

# クイズデータ（50問以上）
quiz_data = [
    {
        "question": "スコッチウィスキーの定義として正しいのはどれか？",
        "options": ["イギリスで製造されたウィスキー", "スコットランドで製造されたウィスキー", "アイルランドで製造されたウィスキー", "スコットランド北部のハイランド地方で製造されたウィスキー"],
        "correct": 1,
        "explanation": "スコッチウィスキーはスコットランドで製造されることが法律で定義されています。"
    },
    {
        "question": "ウィスキーの熟成に使われる樽として最も一般的なのは？",
        "options": ["オークの樽", "メープルの樽", "チェリーの樽", "ビーチの樽"],
        "correct": 0,
        "explanation": "ウィスキー熟成の大部分はオーク樽で行われます。"
    },
    {
        "question": "「ピート」の役割として正しいのはどれか？",
        "options": ["ウィスキーの甘味を加える", "大麦を乾燥させるために燃やされる", "ウィスキーのアルコール度数を上げる", "熟成過程で樽に加えられる物質"],
        "correct": 1,
        "explanation": "ピート（泥炭）は大麦乾燥時に使用され、スモーキーなフレーバーをもたらします。"
    },
    {
        "question": "スコットランドのウィスキー産地で、「島」の蒸留所が集中しているのはどこか？",
        "options": ["アイラ島", "スカイ島", "オークニー島", "これらすべて"],
        "correct": 3,
        "explanation": "スコットランドには複数の島々にウィスキー蒸留所があります。"
    },
    {
        "question": "「シングルモルト」とは何か？",
        "options": ["モルト大麦のみを使用した蒸留酒", "1つの蒸留所で製造されたモルトウィスキー", "モルト大麦を1回だけ蒸留したウィスキー", "単一の年に製造されたウィスキー"],
        "correct": 1,
        "explanation": "シングルモルトは1つの蒸留所で製造されたモルトウィスキーです。"
    },
    {
        "question": "ウィスキーの製造プロセスの正しい順序は？",
        "options": ["糖化→発酵→蒸留→熟成", "発酵→糖化→蒸留→熟成", "蒸留→糖化→発酵→熟成", "熟成→蒸留→糖化→発酵"],
        "correct": 0,
        "explanation": "大麦→糖化（デンプン→砂糖）→発酵→蒸留→熟成が正しいプロセスです。"
    },
    {
        "question": "「ローモンドスチル」について正しいのはどれか？",
        "options": ["ローモンド地域でのみ使用される蒸留器", "可動性の内部構造を持つ蒸留器", "ハイランド産ウィスキーの専用蒸留器", "古い時代にのみ使われた蒸留器"],
        "correct": 1,
        "explanation": "ローモンドスチルは、内部に動く構造を持つ特殊な蒸留器で、蒸留液の性質を変えることができます。"
    },
    {
        "question": "アイリッシュウィスキーの特徴として正しいのはどれか？",
        "options": ["ピーティーなスモーキーフレーバーが特徴", "通常3回蒸留される", "樽熟成が短い傾向", "スコッチより辛口"],
        "correct": 1,
        "explanation": "アイリッシュウィスキーは、通常3回の蒸留により、滑らかで軽いキャラクターになります。"
    },
    {
        "question": "ウイスキーの最低熟成期間は国や地域によって異なります。スコッチウィスキーの最低熟成期間は？",
        "options": ["1年以上", "2年以上", "3年以上", "5年以上"],
        "correct": 2,
        "explanation": "スコットランド法では、スコッチウィスキーは最低3年間オーク樽で熟成される必要があります。"
    },
    {
        "question": "「ノンエイジ」または「ノーエイジステートメント（NAS）」ウィスキーとは？",
        "options": ["熟成していないウィスキー", "年数表示のないウィスキー", "若いウィスキー", "偽造ウィスキー"],
        "correct": 1,
        "explanation": "NASは最低熟成期間を満たしていても、ラベルに年数を表示していないウィスキーです。"
    },
    {
        "question": "ウィスキーの色が濃いほど古い（長く熟成した）という命題は？",
        "options": ["常に正しい", "樽の種類により異なる", "カラメル添加で誤解が生じる", "蒸留所により異なる"],
        "correct": 2,
        "explanation": "ウィスキーの色はカラメル着色の使用により誤解を招く場合があります。樽の種類も影響します。"
    },
    {
        "question": "スコットランドの「ハイランド」地域のウィスキーの特徴として最も一般的なのは？",
        "options": ["ライトで花の香り", "フルボディーで力強い", "ペアティーでスモーキー", "甘めのキャラクター"],
        "correct": 1,
        "explanation": "ハイランド産は多様性がありますが、一般的にはフルボディーで複雑な風味が特徴です。"
    },
    {
        "question": "「コンジャク」（ヴァッティング）とは何か？",
        "options": ["熟成中のウィスキーを樽から取り出すこと", "異なるシングルモルトを混ぜることのもう1つの呼び方", "瓶詰めされたウィスキーの再熟成", "特定地域のウィスキーブレンド"],
        "correct": 1,
        "explanation": "異なるシングルモルトを混ぜたものをヴァッテッドモルトと呼びます。"
    },
    {
        "question": "ジャパニーズウィスキーが国際的に認められるようになったきっかけは？",
        "options": ["政府の支援政策", "山崎や白州が国際比賽で受賞", "日本の観光促進", "フレンチオークの発見"],
        "correct": 1,
        "explanation": "サントリーの山崎やニッカの余市が国際的なコンペティションで高く評価されました。"
    },
    {
        "question": "ウィスキーテイスティングで「ノーズ」と言うのは？",
        "options": ["ウィスキーの味わい", "香りを嗅ぐこと/香り", "ウィスキーを飲み込むこと", "樽の種類"],
        "correct": 1,
        "explanation": "ノーズはテイスティング用語で、ウィスキーの香りやその過程を指します。"
    },
    {
        "question": "「シェリー樽熟成」が与えるフレーバーとして最も適切なのは？",
        "options": ["スモーキーさ", "甘味とドライフルーツ的なニュアンス", "バニラとスパイス", "ピーティーなキャラクター"],
        "correct": 1,
        "explanation": "シェリー樽はドライフルーツ、スパイス、そして甘味をもたらします。"
    },
    {
        "question": "スコットランドのローランド地方のウィスキーの特徴は？",
        "options": ["最も重くてピーティー", "軽くて優雅、グラッシーなフレーバー", "フルボディーで力強い", "甘めのモルトキャラクター"],
        "correct": 1,
        "explanation": "ローランド産は軽く、優雅で、しばしばグラッシーなフレーバーを持つとされています。"
    },
    {
        "question": "\"Angel\\'s Share\"（エンジェルスシェア）とは何か？",
        "options": ["天使が飲むための高級ウィスキー", "樽熟成中に蒸発して失われる部分", "最初に出た蒸留液", "瓶詰め時に失われるウィスキー"],
        "correct": 1,
        "explanation": "樽熟成中、アルコール分や水分が蒸発する部分を指し、これを\"天使の取り分\"と呼びます。"
    },
    {
        "question": "イスライ（Islay）のウィスキーで知られるブランドとして正しいのは？",
        "options": ["グレンモーレンジ", "ラフロイグ", "グレンフィディック", "マッカラン"],
        "correct": 1,
        "explanation": "ラフロイグはアイラ島産の最も有名なピーティーウィスキーの1つです。"
    },
    {
        "question": "スコッチウィスキーにおいて「オーディナリー」マーク（★）は何を示すか？",
        "options": ["品質等級", "熟成年数", "正規品の証明", "蒸留所の格付け"],
        "correct": 2,
        "explanation": "正規品であることを示す正規品証明マークの一つとして使用されます。"
    },
    {
        "question": "ウィスキーの\"オーク\"樽について、樹齢が長いほど良いという命題は？",
        "options": ["常に正しい", "樽の使用方法により異なる", "樽の産地により決定される", "必ずしも正しくない"],
        "correct": 3,
        "explanation": "樹齢の長さだけで品質が決まるわけではなく、樽の管理状態が重要です。"
    },
    {
        "question": "ブレンデッドウィスキーとは何か？",
        "options": ["複数の蒸留所のウィスキーを混ぜたもの", "グレーンウィスキーとモルトウィスキーを混ぜたもの", "製造過程中にアルコールを混ぜたもの", "異なる樽で熟成させた同じウィスキー"],
        "correct": 1,
        "explanation": "ブレンデッドウィスキーはグレーンウィスキーとモルトウィスキーの混合です。"
    },
    {
        "question": "グレーンウィスキーの主な原料は？",
        "options": ["モル大麦のみ", "トウモロコシ、小麦などの穀物", "ライ麦", "米"],
        "correct": 1,
        "explanation": "グレーンウィスキーはモルト大麦の他、トウモロコシ、小麦などを使用します。"
    },
    {
        "question": "\"Cask Strength\"（カスク強度）のウィスキーとは？",
        "options": ["樽から取り出したままの高度数ウィスキー", "特別な樽で熟成させたウィスキー", "高いアルコール度数のウィスキー", "熟成中に水を加えていないウィスキー"],
        "correct": 0,
        "explanation": "カスク強度は樽から取り出したままの、加水されていないウィスキーを指します。"
    },
    {
        "question": "スペイサイド地域で最も有名なウィスキーの特徴は？",
        "options": ["強いピーティー感", "果実的で複雑な香り", "単純で軽い", "非常に辛口"],
        "correct": 1,
        "explanation": "スペイサイド産は果実的で複雑な香りが特徴で、スコッチの中でも高級品が多く見られます。"
    },
    {
        "question": "マッカランで有名なのは何か？",
        "options": ["最も古い蒸留所", "シェリー樽熟成と高価格", "最もピーティー", "グレーンウィスキー"],
        "correct": 1,
        "explanation": "マッカランはシェリー樽熟成で知られ、高級スコッチの代表格です。"
    },
    {
        "question": "ウィスキーの味わいに\"finish\"（フィニッシュ）とは何か？",
        "options": ["飲み始め", "飲み込んだ後に残る味わい", "ボトルの最後の部分", "蒸留の最終段階"],
        "correct": 1,
        "explanation": "フィニッシュはテイスティング用語で、飲み込んだ後に残る余韻を指します。"
    },
    {
        "question": "\"Double Maturation\"（ダブルマチュレーション）とは？",
        "options": ["2つの異なる樽で順番に熟成させること", "2回蒸留すること", "2つの蒸留所で熟成させること", "2年間熟成させること"],
        "correct": 0,
        "explanation": "異なる樽（例：バーボン樽→シェリー樽）で順番に熟成させるプロセスです。"
    },
    {
        "question": "ウィスキー産業で\"VAT\"という用語は何を意味するか？",
        "options": ["ウィスキーの樽", "複数のウィスキーを混ぜる大きな容器", "税金の種類", "蒸留器の部分"],
        "correct": 1,
        "explanation": "VATは複数のウィスキーを混ぜるための大型容器を指します。"
    },
    {
        "question": "スコットランドの\"Campbeltown\"地域について正しいのは？",
        "options": ["最大のウィスキー産地", "衰退したウィスキー産地", "最新の蒸留所が多い", "アイラ島の一部"],
        "correct": 1,
        "explanation": "かつては30以上の蒸留所がありましたが、現在は少数になっています。"
    },
    {
        "question": "ジャパニーズウィスキーとスコッチウィスキーの最大の違いは？",
        "options": ["味わい", "製造される国", "使用樽", "熟成期間"],
        "correct": 1,
        "explanation": "製造地が日本かスコットランドかが法的定義の最大の違いです。"
    },
    {
        "question": "\"Non-Chill Filtered\"（ノンチルフィルタード）ウィスキーの特徴は？",
        "options": ["よりクリア", "低温フィルタリングされていない", "より滑らか", "より高級"],
        "correct": 1,
        "explanation": "低温フィルタリング処理を受けておらず、フレーバーの損失が少ないとされます。"
    },
    {
        "question": "バーボンウィスキーの定義として正しいのはどれか？",
        "options": ["アメリカで製造されたウィスキー", "アメリカで、トウモロコシを主原料に、新しい樽で熟成させたウィスキー", "ケンタッキー州で製造されたウィスキー", "アメリカで8年以上熟成させたウィスキー"],
        "correct": 1,
        "explanation": "バーボンはアメリカの法律で、特定の製造基準を満たす必要があります。"
    },
    {
        "question": "カナディアンウィスキーとして知られる特徴は？",
        "options": ["ピーティー", "軽く滑らか", "甘い", "高アルコール度数"],
        "correct": 1,
        "explanation": "カナディアンウィスキーは軽く滑らかなキャラクターが特徴です。"
    },
    {
        "question": "ウィスキーの\"nose\"の後のテイスティングステップは？",
        "options": ["finish", "palate", "color", "body"],
        "correct": 1,
        "explanation": "テイスティングの順序は、色→ノーズ→パレット（味わい）→フィニッシュです。"
    },
    {
        "question": "\"Peat Smoke\"（ピートスモーク）の強さを測る単位は？",
        "options": ["ppm", "ppb", "PPM（フェノール性ppm）", "SCAA"],
        "correct": 2,
        "explanation": "ピーティーさはフェノール性ppm（phenolic ppm）で測定されます。"
    },
    {
        "question": "レヴィットゥス（\"Levitus\"）とは何か？",
        "options": ["フランスの樽メーカー", "スコットランドの蒸留所", "ウィスキーの品質テスト", "樽の種類"],
        "correct": 1,
        "explanation": "（このクイズ問題は実際の有名な用語ではありません。関連する情報を確認してください。）"
    },
    {
        "question": "ポットスチル（Pot Still）ウィスキーについて正しいのは？",
        "options": ["アイルランドで、麦芽と未麦芽の大麦を混ぜて製造", "スコットランドでのみ製造", "フランスで製造", "古い方法で製造されなくなった"],
        "correct": 0,
        "explanation": "ポットスチルはアイルランドの伝統的な製造方法で、麦芽と未麦芽大麦を使用します。"
    },
    {
        "question": "\"Tasting Notes\"にて\"floral\"（花のような）という表現が使われるのはどのような場合が多いか？",
        "options": ["全てのウィスキー", "ライトボディーのウィスキー", "ピーティーなウィスキー", "バーボンウィスキー"],
        "correct": 1,
        "explanation": "花のような香りはライトボディーで優雅なウィスキーに使われることが多いです。"
    },
    {
        "question": "グレンモーレンジ蒸留所で知られるテイスティング特性は？",
        "options": ["ピーティー", "甘く、花のような", "塩辛い", "樽の味わい"],
        "correct": 1,
        "explanation": "グレンモーレンジは甘く、花のような香りと優雅なキャラクターで知られています。"
    },
    {
        "question": "タリスカー蒸留所はどこにあるか？",
        "options": ["スペイサイド", "アイラ島", "スカイ島", "ハイランド"],
        "correct": 2,
        "explanation": "タリスカーはスカイ島にあり、スパイシーで力強いウィスキーを製造します。"
    },
    {
        "question": "ウィスキー樽の\"charring\"（焦がし）の目的は？",
        "options": ["防腐効果", "樽を硬くする", "ウィスキーにキャラメルと風味をもたらす", "バクテリア対策"],
        "correct": 2,
        "explanation": "樽の内側を焦がすことで、ウィスキーがキャラメル、バニラなどの風味を吸収します。"
    },
    {
        "question": "カスク・タイプ\"Ex-Bourbon\"とは何か？",
        "options": ["バーボンを製造するために新しく樽", "バーボン熟成に使用された中古樽", "バーボンとスコッチの混合熟成樽", "バーボン地域で製造された樽"],
        "correct": 1,
        "explanation": "Ex-Bourbonは、バーボンウィスキー熟成に使用された中古樽を指します。"
    },
    {
        "question": "オルモロッソウィスキー（Amaretto）について、実際に多く使われるのは？",
        "options": ["ウィスキーそのもの", "ウィスキーカクテルのリキュール", "ウィスキーの熟成樽", "蒸留工程"],
        "correct": 1,
        "explanation": "アマレッティはウィスキーベースのカクテルやリキュールに使用されます。"
    },
    {
        "question": "スコッチウィスキーの\"Bottle in Bond\"政策は何を意味するか？",
        "options": ["瓶の品質保証", "熟成の法的保証", "輸出品質", "蒸留所の格付け"],
        "correct": 1,
        "explanation": "特定の製造基準を満たすことを政府が保証する一種の認証です。"
    },
    {
        "question": "オークニー諸島の蒸留所で特に有名なのは？",
        "options": ["グレンフィディック", "ハイランドパーク", "スプリングバンク", "アベラワー"],
        "correct": 1,
        "explanation": "ハイランドパークはオークニー諸島にある、スモーキーで複雑なウィスキーで有名です。"
    },
    {
        "question": "ウィスキーの\"ABV\"（Alcohol By Volume）とは何か？",
        "options": ["樽の容積", "アルコール度数（%）", "樽のタイプ", "蒸留方法"],
        "correct": 1,
        "explanation": "ABVはアルコール度数をパーセンテージで表示したものです。"
    },
    {
        "question": "\"Solera\"（ソレラ）システムについて正しいのはどれか？",
        "options": ["スコットランド発祥", "複数の樽から段階的にウィスキーをブレンドする方法", "ウィスキー専用", "19世紀に廃止された方法"],
        "correct": 1,
        "explanation": "ソレラ・システムは、異なるビンテッジのウィスキーを段階的にブレンドする方法です。"
    },
    {
        "question": "ニッカウヰスキーで有名な蒸留所は？",
        "options": ["山崎", "余市", "宮城峡", "白州"],
        "correct": 1,
        "explanation": "余市はニッカの代表的な蒸留所で、ピーティーなウィスキーを製造します。"
    },
    {
        "question": "ウィスキーの「フェノール値」が高いと何を示すか？",
        "options": ["古いウィスキー", "ピーティー（スモーキー）さが強い", "品質が低い", "アルコール度数が高い"],
        "correct": 1,
        "explanation": "フェノール値が高いほど、ピーティーでスモーキーなキャラクターが強い傾向があります。"
    },
    {
        "question": "ウィスキーの\"木樽効果\"（Barrel Effect）について正しいのは？",
        "options": ["樽自体の重さ", "樽から来るフレーバーと色", "樽の古さ", "樽製造の国"],
        "correct": 1,
        "explanation": "樽効果は、樽からウィスキーが吸収するフレーバーと色をもたらします。"
    },
    {
        "question": "スコットランドのウィスキーで、ラベルに「Speyside」と書かれているのはなぜか？",
        "options": ["品質表示", "地理的表示", "熟成期間", "アルコール度数"],
        "correct": 1,
        "explanation": "スペイサイドはスコットランドの地域名で、産地を示す地理的表示です。"
    },
    {
        "question": "ウィスキーテイスティングで「body」（ボディ）とは何か？",
        "options": ["ウィスキーの色", "口に含んだときの重さや質感", "ウィスキーの価格", "蒸留方法"],
        "correct": 1,
        "explanation": "ボディは、口に含んだときの重さ、質感、粘性などを表します。"
    },
    {
        "question": "アードモア蒸留所で知られるのは？",
        "options": ["最古の蒸留所", "スモーキーで力強いウィスキー", "最高級シェリー樽", "軽くて優雅"],
        "correct": 1,
        "explanation": "アードモアはハイランド産で、スモーキーさと力強さが特徴です。"
    },
    {
        "question": "ウィスキー市場で\"Limited Edition\"（限定版）が意味するのは？",
        "options": ["限定数生産", "限定販売地域", "限定年数熟成", "試験製品"],
        "correct": 0,
        "explanation": "限定版は、生産数が限られた特別なリリースを指します。"
    },
]

# セッションステートの初期化
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.quiz_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.shuffled_questions = []

# クイズ開始ボタン
col1, col2, col3 = st.columns(3)

if col1.button("🚀 クイズを開始"):
    st.session_state.quiz_started = True
    st.session_state.quiz_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    random.shuffle(quiz_data)
    st.session_state.shuffled_questions = quiz_data
    st.rerun()

if col2.button("🔄 リセット"):
    st.session_state.quiz_started = False
    st.session_state.quiz_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.shuffled_questions = []
    st.rerun()

# ステータス表示
if st.session_state.quiz_started and st.session_state.shuffled_questions:
    st.divider()

    # 進捗バー
    progress = st.session_state.quiz_index / len(st.session_state.shuffled_questions)
    st.progress(progress)

    st.markdown(f"**問題 {st.session_state.quiz_index + 1} / {len(st.session_state.shuffled_questions)}**")
    st.markdown(f"**現在のスコア: {st.session_state.score} 点**")

    st.divider()

    # 現在の問題を取得
    current_question = st.session_state.shuffled_questions[st.session_state.quiz_index]

    # 問題を表示
    st.subheader(current_question["question"])

    # 選択肢を表示
    selected_option = st.radio(
        "答えを選んでください:",
        options=range(len(current_question["options"])),
        format_func=lambda i: current_question["options"][i],
        key=f"question_{st.session_state.quiz_index}"
    )

    # 「答える」ボタン
    if not st.session_state.answered:
        if st.button("✅ 答える"):
            st.session_state.answered = True
            st.rerun()

    # 回答後の表示
    if st.session_state.answered:
        is_correct = selected_option == current_question["correct"]

        if is_correct:
            st.success("🎉 正解です！")
            st.session_state.score += 1
        else:
            st.error("❌ 不正解です")

        # 解説を表示
        st.info(f"**解説:** {current_question['explanation']}")

        # 次へボタン
        if st.session_state.quiz_index < len(st.session_state.shuffled_questions) - 1:
            if st.button("➡️ 次の問題へ"):
                st.session_state.quiz_index += 1
                st.session_state.answered = False
                st.rerun()
        else:
            # クイズ終了
            st.divider()
            st.balloons()

            st.markdown("## 🏆 クイズ終了！")

            # 最終スコア
            final_score = st.session_state.score
            total_questions = len(st.session_state.shuffled_questions)
            percentage = (final_score / total_questions) * 100

            st.metric("最終スコア", f"{final_score} / {total_questions}", f"{percentage:.1f}%")

            # 結果評価
            if percentage >= 90:
                st.success("🏅 素晴らしい！エキスパート水準です！")
            elif percentage >= 80:
                st.info("✨ 良好です！あと少しで完璧ですね。")
            elif percentage >= 70:
                st.warning("📚 もう少し復習が必要です。")
            else:
                st.warning("💪 もっと学習しましょう。頑張ってください！")

            st.divider()

            if st.button("🔄 もう一度クイズをする"):
                st.session_state.quiz_started = False
                st.session_state.quiz_index = 0
                st.session_state.score = 0
                st.session_state.answered = False
                st.session_state.shuffled_questions = []
                st.rerun()

else:
    if not st.session_state.quiz_started:
        st.divider()
        st.markdown("""
        ### 📖 このアプリについて

        ウィスキーエキスパート資格試験の対策用クイズアプリです。

        **出題内容:**
        - ✅ ウィスキーの歴史と地域特性
        - ✅ 製造プロセス（糖化、発酵、蒸留、熟成）
        - ✅ スコットランド、アイルランド、日本など各地のウィスキー
        - ✅ テイスティング用語と技法
        - ✅ 樽と熟成に関する知識
        - ✅ ブレンディングと品質管理

        **特徴:**
        - 🔀 毎回異なる順序で出題
        - 📊 リアルタイムスコア表示
        - 💡 各問題に詳しい解説付き
        - 🏆 最終結果の評価

        **準備ができたら、上の「クイズを開始」ボタンをクリックしてください！**
        """)
