// Generated by gencpp from file phidgets/lidar_control.msg
// DO NOT EDIT!


#ifndef PHIDGETS_MESSAGE_LIDAR_CONTROL_H
#define PHIDGETS_MESSAGE_LIDAR_CONTROL_H

#include <ros/service_traits.h>


#include <phidgets/lidar_controlRequest.h>
#include <phidgets/lidar_controlResponse.h>


namespace phidgets
{

struct lidar_control
{

typedef lidar_controlRequest Request;
typedef lidar_controlResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct lidar_control
} // namespace phidgets


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::phidgets::lidar_control > {
  static const char* value()
  {
    return "63541d856b007db47fcb5fb28b699f7b";
  }

  static const char* value(const ::phidgets::lidar_control&) { return value(); }
};

template<>
struct DataType< ::phidgets::lidar_control > {
  static const char* value()
  {
    return "phidgets/lidar_control";
  }

  static const char* value(const ::phidgets::lidar_control&) { return value(); }
};


// service_traits::MD5Sum< ::phidgets::lidar_controlRequest> should match 
// service_traits::MD5Sum< ::phidgets::lidar_control > 
template<>
struct MD5Sum< ::phidgets::lidar_controlRequest>
{
  static const char* value()
  {
    return MD5Sum< ::phidgets::lidar_control >::value();
  }
  static const char* value(const ::phidgets::lidar_controlRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::phidgets::lidar_controlRequest> should match 
// service_traits::DataType< ::phidgets::lidar_control > 
template<>
struct DataType< ::phidgets::lidar_controlRequest>
{
  static const char* value()
  {
    return DataType< ::phidgets::lidar_control >::value();
  }
  static const char* value(const ::phidgets::lidar_controlRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::phidgets::lidar_controlResponse> should match 
// service_traits::MD5Sum< ::phidgets::lidar_control > 
template<>
struct MD5Sum< ::phidgets::lidar_controlResponse>
{
  static const char* value()
  {
    return MD5Sum< ::phidgets::lidar_control >::value();
  }
  static const char* value(const ::phidgets::lidar_controlResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::phidgets::lidar_controlResponse> should match 
// service_traits::DataType< ::phidgets::lidar_control > 
template<>
struct DataType< ::phidgets::lidar_controlResponse>
{
  static const char* value()
  {
    return DataType< ::phidgets::lidar_control >::value();
  }
  static const char* value(const ::phidgets::lidar_controlResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // PHIDGETS_MESSAGE_LIDAR_CONTROL_H