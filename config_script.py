from mw2fcitx.tweaks.moegirl import tweaks

exports = {
    "source": {
        "api_path": "https://wiki.biligame.com/ys/api.php",
        "kwargs": {
            "partial": "partial.json",
            "output": "titles.txt",
            "request_delay": 30,
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.4 Mobile/15E148 Safari/604.1",
            "api_params": {
                "aplimit": "max"
            }
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
