from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://wiki.biligame.com/ys/api.php",
        "kwargs": {
            "partial": "partial.json",
            "output": "titles.txt",
            "request_delay": 3,
            "user_agent": "RimeLunaPinyinCustomDict-GitHubAction/1.0 (https://github.com/qvshuo/rime-luna-pinyin-custom-dict)"
        }
    },
    "tweaks": tweaks,
    "converter": {
        "use": "pypinyin",
        "kwargs": {}
    },
    "generator": [{
        "use": "rime",
        "kwargs": {
            "output": "yuanshen.dict.yaml"
        }
    }]
}
