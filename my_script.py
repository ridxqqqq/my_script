# my_script.py
import requests
from datetime import datetime

myKey = '&key=d69dcdd27f13496dbf2d13036b2d838b'  # 和风天气Key
City = 'location=101050806'  # 伊春南岔代码

url_api_weather = 'https://devapi.qweather.com/v7/weather/now?'  # 实时天气
url_api_3dweather = 'https://devapi.qweather.com/v7/weather/3d?'  # 3天天气
url_api_air = 'https://devapi.qweather.com/v7/air/now?'  # 实时空气质量


def get_now_weather():  # 实时天气
    url = url_api_weather + City + myKey
    # print(url)
    return requests.get(url).json()


def get_3day_weather():  # 3天天气
    url = url_api_3dweather + City + myKey
    return requests.get(url).json()


def get_air():  # 空气质量
    url = url_api_air + City + myKey
    return requests.get(url).json()

if __name__ == '__main__':
    CurrentWeather = get_now_weather()
    ThreeDayWeather = get_3day_weather()
    CurrentAirLevel = get_air()
    URL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ce4804e3-9d04-4fb9-be0d-56ae58067ffb'
    mHeader = {'Content-Type': 'application/json; charset=UTF-8'}
    mBody = {
        "msgtype": "text",
        "text": {
            "content": '当前时间:' + datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S') + '\n' + '南岔县天气预报:' + '\n' + '\n' + '当前温度:' + CurrentWeather['now'][
                'temp'] + '\n' + '当前体感温度:' +
                       CurrentWeather['now']['feelsLike'] + '\n' + '天气状况:' +
                       CurrentWeather['now']['text'] + '\n' + '相对湿度:' + CurrentWeather['now'][
                           'humidity'] + '\n' + '累计降水量:' + CurrentWeather['now'][
                           'precip'] + '\n' + '空气质量指数:' +
                       CurrentAirLevel['now']['aqi'] + '\n' + '未来三天天气情况:' + '\n' + ThreeDayWeather['daily'][0][
                           'fxDate'] + ':' + '\n' + '温度:' + ThreeDayWeather['daily'][0]['tempMin'] + '℃~' +
                       ThreeDayWeather['daily'][0]['tempMax'] + '℃' + '\n' + '天气状况:' + ThreeDayWeather['daily'][0][
                           'textDay'] + '\n' + ThreeDayWeather['daily'][1]['fxDate'] + ':' + '\n' + '温度:' +
                       ThreeDayWeather['daily'][1]['tempMin'] + '℃~' +
                       ThreeDayWeather['daily'][1]['tempMax'] + '℃' + '\n' + '天气状况:' + ThreeDayWeather['daily'][1][
                           'textDay'] + '\n' + ThreeDayWeather['daily'][2]['fxDate'] + ':' + '\n' + '温度:' +
                       ThreeDayWeather['daily'][2]['tempMin'] + '℃~' +
                       ThreeDayWeather['daily'][2]['tempMax'] + '℃' + '\n' + '天气状况:' + ThreeDayWeather['daily'][2][
                           'textDay'] + '\n' + '\n' + '更新时间:' + '\n' +
                       CurrentWeather[
                           'updateTime']
        }
    }
    # 注意：json=mBody  必须用json
    requests.post(url=URL, json=mBody, headers=mHeader)

    # print(CurrentWeather)
    print('伊春市', '南岔县')
    print('当前温度:', CurrentWeather['now']['temp'] + '\n', '当前体感温度:', CurrentWeather['now']['feelsLike'] + '\n',
          '天气状况:',
          CurrentWeather['now']['text'])
    print('相对湿度:', CurrentWeather['now']['humidity'] + '\n', '累计降水量:', CurrentWeather['now']['precip'] + '\n',
          '空气质量指数:',
          CurrentAirLevel['now']['aqi'])
    print('未来三天天气情况:')
    print(ThreeDayWeather['daily'][0]['fxDate'] + ':' + '温度:', ThreeDayWeather['daily'][0]['tempMin'] + '℃~' +
          ThreeDayWeather['daily'][0]['tempMax'] + '℃', '天气状况:', ThreeDayWeather['daily'][0]['textDay'])
    print(ThreeDayWeather['daily'][1]['fxDate'] + ':' + '温度:', ThreeDayWeather['daily'][1]['tempMin'] + '℃~' +
          ThreeDayWeather['daily'][1]['tempMax'] + '℃', '天气状况:', ThreeDayWeather['daily'][1]['textDay'])
    print(ThreeDayWeather['daily'][2]['fxDate'] + ':' + '温度:', ThreeDayWeather['daily'][2]['tempMin'] + '℃~' +
          ThreeDayWeather['daily'][2]['tempMax'] + '℃', '天气状况:', ThreeDayWeather['daily'][2]['textDay'])
    print('更新时间:', CurrentWeather['updateTime'])
